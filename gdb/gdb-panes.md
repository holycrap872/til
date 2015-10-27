# GDB Panes

When debugging code, it can be helpful to have access to *all* of the information that can.
This includes both the source code as well as its underlying assembly.  GDB allows you to
access this information using various layouts.  The default layout (a command pane with a
source code pane about it) can be accessed by simply running `gdb -tui`.  You can then type
the normal gdb commands while viewing where you are in the source simultaneously.  The list
of commands below, however, allows you to access a much greater variety of information.

1) `layout next`: This cycles through GDB's layout until you find one that is of particular
interest.

2) `focus {CMD, SRC, REG, ASM}`: This puts the focus on various panes in the GDB window so that
the up down arrows can be used.  For example `focus CMD` allows you to cycle through previous
instructions whereas `focus SRC` lets you move up and down in the source file.

Note: Sometimes GDB will get a little blocky, seeming to combine the code from previous
functions into a single, unreadable screen.  I've found that focusing on the messed up
window and moving up and down with the arrow keys seems to usually fix to the problem.

# Best Practices accoring to _Programming in Python 3_

1) Don't do `from X import w, y, z`.  Instead do `import x` and use the fully
qualified name in the program.  This avoids name collisions.

2) Have own modules start with an upper-case letter since lower-case as usually
used by the standard libary.

3) 

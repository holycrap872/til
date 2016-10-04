# WTF
So you're seeing the follwing error

```
warning: incompatible implicit declaration of built-in function ‘exit’ [enabled by default]
```

This meant that I hadn't included the correct header (`stdlib.h`) in my file.
Why didn't it just say `warning: implicit declaration`?  The reason for this
seems to be that gcc includes in it's compilation process information on
common c functions (exit being one of them).  It seems to be trying to
alert me that there is likely a common function that will do what I want that
already exists.

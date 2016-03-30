# Python Modules

I miss the structure that java provides in it's packages.  I have the tendency
of using the freedom of python to do some very ugly things that are then very
difficult to clean up later.  For example, I've never used python modules before,
mostly keeping my scripts below 100 lines.  Now that I'm doing a lot of work
in python, however, this is no longer sustainable.  Therefore, I'm going to
start using python modules.

## How modules work

Modules work in a similar way to java's packages.  The key is to have a
`__init__.py` file at every level of the "package".  With these files in place
you can then use relative addressing to the file you're importing.  For example:

```
package_name
    - __init__.py
    - thing1.py
    - thing2.py
    - lib
        - __init__.py
        - util.py
```

In this case, the package_name is the name of the top-level folder.  In order
to access the `util.py` file, all you need to do is `import package_name.lib.util`

## Getting Fancy

The `__init__.py` can be empty.  This gives you basic "relative path" access
to the contents of the package.  You can, however, put stuff in the __init__.py
file.  For example, you could do something like

```
from thing1 import *
from thing2 import parser
from lib.util import helper_function
```

This means that when you simply type `import package_name` from some outside
python file, you get access to `parser`, `helper_function` and everything in
thing1 without having to identify them by the file they are in. 

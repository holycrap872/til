# Communicating with Low-level c stuff

You can used python to communicate with low-level c program using the normal
`open`, `pipe`, `dup2`, `close` linux functions with the os module.

An example is below

Python

```
import os
import struct
import subprocess

read_py_fd, write_c_fd = os.pipe()
read_c_fd, write_py_fd = os.pipe()

read_py_fd = os.fdopen(read_py_fd, "rb")
write_py_fd = os.fdopen(write_py_fd, "wb")

os.dup2(read_c_fd, READ_C_FD)
os.set_inheritable(READ_C_FD, True)
os.dup2(write_c_fd, WRITE_C_FD)
os.set_inheritable(WRITE_C_FD, True)

subprocess.Popen(cmd,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.STDOUT,
                 close_fds=False,  # **important**
                 )

write_py_fd.write(struct.pack("I", value))
ret = struct.unpack("I",  read_py_fd.read(4))[0]

```

C

```
int readval;
if (read(READ_C_FD, &read_val, 4) != 4) exit(1);

read_val++;

if (write(WRITE_C_FD, &read_val, 4) != 4) exit(1);
```

In these examples, read_py_int is a file descriptor in the traditional c form,
i.e. just a number.  In order to have python work with this, you need to use
the special `os.fdopen` method, rather than just `open`.

In addition, python by default shuts down all fd's on when it kicks off a
subprocess.  In order to keep all your hard work, make sure you make them
"inheritable" for the child processes *and* you use `close_fds=False` in the
subprocess Popen command.


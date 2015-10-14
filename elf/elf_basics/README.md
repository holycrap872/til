# Explanation

This folder is a little bit different than my other til's.  In this case, I am experimenting
on various headers and examining their output.  Therefore, I have set up this folder as an
analysis of various programs.  Each of these analysis's may reference each other.

## What is ELF?

ELF is a way of storing a program in one of several different forms.  An ELF file
consists of an ELF header, which is used to given a description of how the ELF file
is laid out an for whom it was compiled.  This file header can be used to find the
two main ways that ELF organizes the program, the Program Header (comes right after
the file header) and the Section Header (comes at the end of the ELF file).  The
Program Header is used to describe how the program is ordered in terms of segments
(discussed later).  The Section Header is used to describe how the program is ordered
in terms of sections (again, discussed later).  These headers act on the same information,
but order it in different ways.

An ELF file can be:

1. An executable `gcc -o hello hello.c`

2. A library file `gcc `

3. A temporay `gcc `

From each of these three commands, a different version of an elf program is created.  The best
explanation I have found so far is in the form of a picture, courtesy of of OpenSecurityTraining.

```
Picture here
```

This shows that, depending on it's form, the ELF can be viewed either in terms of Sections
(library) or in terms of Segments (executable).  When it's viewed as a library, the Sections
map points to individual chucks of code.  As of right now (because it could be wrong), these
Sections seem to be roughly analogous to functions within the compiled file.  The Sections
map allows calling files to pull in different pieces from other files as needed.  Segements,
on the other hand, are composed of the parts of the code that are needed for a particular
execution.  Segments include the 0x400000 block (the code and read-only data associated with the
executable) and the 0x600000 block (the code associated with global variables in the executable).



##Analysing `hello.c` as an executable

Program: [hello.c](hello.c)

ELF: [hello](hello)

Examining the ELF Header: [readelf -h hello](readelf_-f_hello.md)

Examining the Program Headers : [readelf -l hello](readelf_-l_hello.md)

Examining the Binary: [objdump -D hello](objdump_-D_hello.md)

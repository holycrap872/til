# Readelf -S hello

```
There are 30 section headers, starting at offset 0x1198:

Section Headers:
  [Nr] Name              Type             Address           Offset
       Size              EntSize          Flags  Link  Info  Align
  [ 0]                   NULL             0000000000000000  00000000
       0000000000000000  0000000000000000           0     0     0
  [ 1] .interp           PROGBITS         0000000000400238  00000238
       000000000000001c  0000000000000000   A       0     0     1
```

#### Observations

1. The section specifying the interpreter.  This is necessary for dynamic
linking when a program is running/about to be run.  This is such an important
section that the Program Header points to it.

2. In a similar way, the .dynamic section ([21]) is used for something...
at this point to be honest I'm not sure what.

```
  [ 2] .note.ABI-tag     NOTE             0000000000400254  00000254
       0000000000000020  0000000000000000   A       0     0     4
  [ 3] .note.gnu.build-i NOTE             0000000000400274  00000274
       0000000000000024  0000000000000000   A       0     0     4
  [ 4] .gnu.hash         GNU_HASH         0000000000400298  00000298
       000000000000001c  0000000000000000   A       5     0     8
```

#### Observations

1. The .hash table contains the symbol hash table.  This (although I'm
not sure yet) is likely used during runtime to quickly retrieve particular
symbols when jumping, linking, or reading.

```
  [ 5] .dynsym           DYNSYM           00000000004002b8  000002b8
       0000000000000060  0000000000000018   A       6     1     8
  [ 6] .dynstr           STRTAB           0000000000400318  00000318
       000000000000003d  0000000000000000   A       0     0     1
```

#### Observations

1.  The .dynstr section is very important for identifying the funtion/
libraries that should be linked during dynamic linking.

2. The .dymsym section contains the dynamic linking symbol table.

```
  [ 7] .gnu.version      VERSYM           0000000000400356  00000356
       0000000000000008  0000000000000002   A       5     0     2
  [ 8] .gnu.version_r    VERNEED          0000000000400360  00000360
       0000000000000020  0000000000000000   A       6     1     8
  [ 9] .rela.dyn         RELA             0000000000400380  00000380
       0000000000000018  0000000000000018   A       5     0     8
  [10] .rela.plt         RELA             0000000000400398  00000398
       0000000000000048  0000000000000018   A       5    12     8
  [11] .init             PROGBITS         00000000004003e0  000003e0
       000000000000001a  0000000000000000  AX       0     0     4
```

#### Observation

1. The .init section is associated with initializing a runtime environment
while the .finit section is associated with tearing down the environment.

```
  [12] .plt              PROGBITS         0000000000400400  00000400
       0000000000000040  0000000000000010  AX       0     0     16
  [13] .text             PROGBITS         0000000000400440  00000440
       0000000000000172  0000000000000000  AX       0     0     16

```

#### Observation

1. This section is associated with the code of the program.

```

  [14] .fini             PROGBITS         00000000004005b4  000005b4
       0000000000000009  0000000000000000  AX       0     0     4
  [15] .rodata           PROGBITS         00000000004005c0  000005c0
       0000000000000011  0000000000000000   A       0     0     4
```

#### Observations

1. This section is associated with read-only data.  Usually this contains
constant string.

``
  [16] .eh_frame_hdr     PROGBITS         00000000004005d4  000005d4
       0000000000000034  0000000000000000   A       0     0     4
  [17] .eh_frame         PROGBITS         0000000000400608  00000608
       00000000000000f4  0000000000000000   A       0     0     8
```

##### Observations

1. Here the program splits.  Everything above can be thought of as
executable code and everything below can be through of as data.  The
hole in between is basically up for grabs.  It might be used for heap?
I know it isn't used for stack because stack goes from the end of the
data section (in this instance, 0x601048 and up).

```
  [18] .init_array       INIT_ARRAY       0000000000600e10  00000e10
       0000000000000008  0000000000000000  WA       0     0     8
  [19] .fini_array       FINI_ARRAY       0000000000600e18  00000e18
       0000000000000008  0000000000000000  WA       0     0     8
  [20] .jcr              PROGBITS         0000000000600e20  00000e20
       0000000000000008  0000000000000000  WA       0     0     8
  [21] .dynamic          DYNAMIC          0000000000600e28  00000e28
       00000000000001d0  0000000000000010  WA       6     0     8
  [22] .got              PROGBITS         0000000000600ff8  00000ff8
       0000000000000008  0000000000000008  WA       0     0     8
  [23] .got.plt          PROGBITS         0000000000601000  00001000
       0000000000000030  0000000000000008  WA       0     0     8
  [24] .data             PROGBITS         0000000000601030  00001030
       0000000000000010  0000000000000000  WA       0     0     8
  [25] .bss              NOBITS           0000000000601040  00001040
       0000000000000008  0000000000000000  WA       0     0     1
```

#### Observations

1. The .data section is associated with global variables whose values have
been defined in the program.

2. The .bss section is defined for global variables that haven't been initialized yet.
Essentially, it's just empty space to be filled later.

```
  [26] .comment          PROGBITS         0000000000000000  00001040
       000000000000004d  0000000000000001  MS       0     0     1
  [27] .shstrtab         STRTAB           0000000000000000  0000108d
       0000000000000108  0000000000000000           0     0     1
  [28] .symtab           SYMTAB           0000000000000000  00001918
       0000000000000618  0000000000000018          29    45     8
  [29] .strtab           STRTAB           0000000000000000  00001f30
       0000000000000237  0000000000000000           0     0     1
```

#### Observations

1. The preceeding three sections are interesting because they contain
strings that are used for various purposes during runtime that aren't
seen in the source code.

2. The .shstrab constains section header string tables.  Each section
simply references a section in this table in order to identify itself.
This setup allows sections to have names that are REALLY long.  This
is counter to the way other file formats which allocated a certain
number of bits for a name, limiting their potential size.

3. The .symtab contains "non-dynamic linking information".  This information
can therefore be removed during normal execution (via `strip`) since the
destination address is known.

4. The .strtab is another string table containing "non-dynamic linked symbol
names".  Like the previously discussed section, this can be removed
with the `strip` utility without affecting performance.

```
Key to Flags:
  W (write), A (alloc), X (execute), M (merge), S (strings), l (large)
  I (info), L (link order), G (group), T (TLS), E (exclude), x (unknown)
  O (extra OS processing required) o (OS specific), p (processor specific)
```

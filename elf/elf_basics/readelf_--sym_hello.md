# Readelf --sym hello && Readelf --sym hellostrip

```
Symbol table '.dynsym' contains 4 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND 
     1: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.2.5 (2)
     2: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@GLIBC_2.2.5 (2)
     3: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__

Symbol table '.symtab' contains 65 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND 
     1: 0000000000400238     0 SECTION LOCAL  DEFAULT    1 
     2: 0000000000400254     0 SECTION LOCAL  DEFAULT    2 
     3: 0000000000400274     0 SECTION LOCAL  DEFAULT    3 
     4: 0000000000400298     0 SECTION LOCAL  DEFAULT    4 
     5: 00000000004002b8     0 SECTION LOCAL  DEFAULT    5 
     6: 0000000000400318     0 SECTION LOCAL  DEFAULT    6 
     7: 0000000000400356     0 SECTION LOCAL  DEFAULT    7 
     8: 0000000000400360     0 SECTION LOCAL  DEFAULT    8 
     9: 0000000000400380     0 SECTION LOCAL  DEFAULT    9 
    10: 0000000000400398     0 SECTION LOCAL  DEFAULT   10 
    11: 00000000004003e0     0 SECTION LOCAL  DEFAULT   11 
    12: 0000000000400400     0 SECTION LOCAL  DEFAULT   12 
    13: 0000000000400440     0 SECTION LOCAL  DEFAULT   13 
    14: 00000000004005b4     0 SECTION LOCAL  DEFAULT   14 
    15: 00000000004005c0     0 SECTION LOCAL  DEFAULT   15 
    16: 00000000004005d4     0 SECTION LOCAL  DEFAULT   16 
    17: 0000000000400608     0 SECTION LOCAL  DEFAULT   17 
    18: 0000000000600e10     0 SECTION LOCAL  DEFAULT   18 
    19: 0000000000600e18     0 SECTION LOCAL  DEFAULT   19 
    20: 0000000000600e20     0 SECTION LOCAL  DEFAULT   20 
    21: 0000000000600e28     0 SECTION LOCAL  DEFAULT   21 
    22: 0000000000600ff8     0 SECTION LOCAL  DEFAULT   22 
    23: 0000000000601000     0 SECTION LOCAL  DEFAULT   23 
    24: 0000000000601030     0 SECTION LOCAL  DEFAULT   24 
    25: 0000000000601040     0 SECTION LOCAL  DEFAULT   25 
    26: 0000000000000000     0 SECTION LOCAL  DEFAULT   26 
    27: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    28: 0000000000600e20     0 OBJECT  LOCAL  DEFAULT   20 __JCR_LIST__
    29: 0000000000400470     0 FUNC    LOCAL  DEFAULT   13 deregister_tm_clones
    30: 00000000004004a0     0 FUNC    LOCAL  DEFAULT   13 register_tm_clones
    31: 00000000004004e0     0 FUNC    LOCAL  DEFAULT   13 __do_global_dtors_aux
    32: 0000000000601040     1 OBJECT  LOCAL  DEFAULT   25 completed.6973
    33: 0000000000600e18     0 OBJECT  LOCAL  DEFAULT   19 __do_global_dtors_aux_fin
    34: 0000000000400500     0 FUNC    LOCAL  DEFAULT   13 frame_dummy
    35: 0000000000600e10     0 OBJECT  LOCAL  DEFAULT   18 __frame_dummy_init_array_
    36: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS hello.c
    37: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS crtstuff.c
    38: 00000000004006f8     0 OBJECT  LOCAL  DEFAULT   17 __FRAME_END__
    39: 0000000000600e20     0 OBJECT  LOCAL  DEFAULT   20 __JCR_END__
    40: 0000000000000000     0 FILE    LOCAL  DEFAULT  ABS 
    41: 0000000000600e18     0 NOTYPE  LOCAL  DEFAULT   18 __init_array_end
    42: 0000000000600e28     0 OBJECT  LOCAL  DEFAULT   21 _DYNAMIC
    43: 0000000000600e10     0 NOTYPE  LOCAL  DEFAULT   18 __init_array_start
    44: 0000000000601000     0 OBJECT  LOCAL  DEFAULT   23 _GLOBAL_OFFSET_TABLE_
    45: 00000000004005b0     2 FUNC    GLOBAL DEFAULT   13 __libc_csu_fini
    46: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_deregisterTMCloneTab
    47: 0000000000601030     0 NOTYPE  WEAK   DEFAULT   24 data_start
    48: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@@GLIBC_2.2.5
    49: 0000000000601040     0 NOTYPE  GLOBAL DEFAULT   24 _edata
    50: 00000000004005b4     0 FUNC    GLOBAL DEFAULT   14 _fini
    51: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@@GLIBC_
    52: 0000000000601030     0 NOTYPE  GLOBAL DEFAULT   24 __data_start
    53: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
    54: 0000000000601038     0 OBJECT  GLOBAL HIDDEN    24 __dso_handle
    55: 00000000004005c0     4 OBJECT  GLOBAL DEFAULT   15 _IO_stdin_used
    56: 0000000000400540   101 FUNC    GLOBAL DEFAULT   13 __libc_csu_init
    57: 0000000000601048     0 NOTYPE  GLOBAL DEFAULT   25 _end
    58: 0000000000400440     0 FUNC    GLOBAL DEFAULT   13 _start
    59: 0000000000601040     0 NOTYPE  GLOBAL DEFAULT   25 __bss_start
    60: 000000000040052d    16 FUNC    GLOBAL DEFAULT   13 main
    61: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _Jv_RegisterClasses
    62: 0000000000601040     0 OBJECT  GLOBAL HIDDEN    24 __TMC_END__
    63: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND _ITM_registerTMCloneTable
    64: 00000000004003e0     0 FUNC    GLOBAL DEFAULT   11 _init
```

The symbol table associated with a stripped binary.  Clearly there is much less
information related to .symtab (none).  The dynamic sym table, which calls outside
libraries, is still required, however.

```
Symbol table '.dynsym' contains 4 entries:
   Num:    Value          Size Type    Bind   Vis      Ndx Name
     0: 0000000000000000     0 NOTYPE  LOCAL  DEFAULT  UND 
     1: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND puts@GLIBC_2.2.5 (2)
     2: 0000000000000000     0 FUNC    GLOBAL DEFAULT  UND __libc_start_main@GLIBC_2.2.5 (2)
     3: 0000000000000000     0 NOTYPE  WEAK   DEFAULT  UND __gmon_start__
```

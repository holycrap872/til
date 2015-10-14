#Readelf -l Breakdown

When I ran `readelf -l hello`, I got the following output.  I intersperse
my comments with references to the [objdump](objdump.md)

```
Elf file type is EXEC (Executable file)
Entry point 0x400440
There are 9 program headers, starting at offset 64

Program Headers:
  Type           Offset             VirtAddr           PhysAddr
                 FileSiz            MemSiz              Flags  Align
  PHDR           0x0000000000000040 0x0000000000400040 0x0000000000400040
                 0x00000000000001f8 0x00000000000001f8  R E    8
```

Observations
1) Based on the readelf -h, the elf header information is 64 bytes.  Thus the
   0x40 start address of PHDR
2) Based on the readelf -h, there are 9 programs heads, each header taking up
   56 bytes.  56 * 9 -> 504 -> 0x1f8
3) Based on opensecuritytraining.info, this section doesn't get mapped into
   memory, so VirtAddr = PhysAddr since it doesn't matter.
4) This section is R E.  It won't be mapped into memory, however, so this
   doesn't really matter.

```
  INTERP         0x0000000000000238 0x0000000000400238 0x0000000000400238
                 0x000000000000001c 0x000000000000001c  R      1
      [Requesting program interpreter: /lib64/ld-linux-x86-64.so.2]
```

Observations:
1) INTERP offset = 64 (elf header) + 504 (program header) = 0x238
2) Readelf pulls out this string here.  This is the interpreter that is going
   to be used toa dynamically link this particular binary.  This will be
   be loaded into memory before the rest of the binary.

```
  LOAD           0x0000000000000000 0x0000000000400000 0x0000000000400000
                 0x00000000000006fc 0x00000000000006fc  R E    200000
  LOAD           0x0000000000000e10 0x0000000000600e10 0x0000000000600e10
                 0x0000000000000230 0x0000000000000238  RW     200000
```

Observations
1) These say what values get loaded into memory.  There are two loads, basically
   throwing certain parts of the program from the ELF file into memory.
2) These VirtAddr's map exactly onto the addresses you get when running objdump
   -D.  The first load corresponds with addresses 0x400238 - 0x400700.  The reason 
   I'm guessing that it's not 0x4006fc is there's some padding thrown in there.
   The second load corresponds to 0x600e10 - 0x601038.
3) It's obviously not magic that the obj-dump maps so closely to these values.
   It's likely that objdump dynamically generates what the virtual file would
   look like upon being loaded into memory.

```
  DYNAMIC        0x0000000000000e28 0x0000000000600e28 0x0000000000600e28
                 0x00000000000001d0 0x00000000000001d0  RW     8
  NOTE           0x0000000000000254 0x0000000000400254 0x0000000000400254
                 0x0000000000000044 0x0000000000000044  R      4
  GNU_EH_FRAME   0x00000000000005d4 0x00000000004005d4 0x00000000004005d4
                 0x0000000000000034 0x0000000000000034  R      4
  GNU_STACK      0x0000000000000000 0x0000000000000000 0x0000000000000000
                 0x0000000000000000 0x0000000000000000  RW     10
  GNU_RELRO      0x0000000000000e10 0x0000000000600e10 0x0000000000600e10
                 0x00000000000001f0 0x00000000000001f0  R      1

 Section to Segment mapping:
  Segment Sections...
   00     
   01     .interp 
   02     .interp .note.ABI-tag .note.gnu.build-id .gnu.hash .dynsym .dynstr .gnu.version .gnu.version_r .rela.dyn .rela.plt .init .plt .text .fini .rodata .eh_frame_hdr .eh_frame 
   03     .init_array .fini_array .jcr .dynamic .got .got.plt .data .bss 
   04     .dynamic 
   05     .note.ABI-tag .note.gnu.build-id 
   06     .eh_frame_hdr 
   07     
   08     .init_array .fini_array .jcr .dynamic .got 
```

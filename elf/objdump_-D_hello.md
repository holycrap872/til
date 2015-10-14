# Objdump Breakdown

When I ran `objdump -D hello`, I got the following output.  I intersperse
my comments with references to [readelf -l hello](readelf_-l_hello.md) and
[readelf -h hello](readelf_-h_hello.md).

```
hello:     file format elf64-x86-64


Disassembly of section .interp:

0000000000400238 <.interp>:
```

#### Observation

1. Based on opensecuritytraining.info, when the program gets actually loaded
into memory, even though the start address is 0x400238, the OS grabs the program
in 1000 byte chunks.  This means that stuff like the ELF magic number will
likely be grabbed and through into address 0x400000.  This can be examined by
running `gdb hello`, `break main` `r` `x/8 0x400000`.

```
  400238:	2f                   	(bad)  
  400239:	6c                   	insb   (%dx),%es:(%rdi)
  40023a:	69 62 36 34 2f 6c 64 	imul   $0x646c2f34,0x36(%rdx),%esp
  400241:	2d 6c 69 6e 75       	sub    $0x756e696c,%eax
  400246:	78 2d                	js     400275 <_init-0x16b>
  400248:	78 38                	js     400282 <_init-0x15e>
  40024a:	36                   	ss
  40024b:	2d 36 34 2e 73       	sub    $0x732e3436,%eax
  400250:	6f                   	outsl  %ds:(%rsi),(%dx)
  400251:	2e 32 00             	xor    %cs:(%rax),%al

Disassembly of section .note.ABI-tag:

0000000000400254 <.note.ABI-tag>:
  400254:	04 00                	add    $0x0,%al
  400256:	00 00                	add    %al,(%rax)
  400258:	10 00                	adc    %al,(%rax)
  40025a:	00 00                	add    %al,(%rax)
  40025c:	01 00                	add    %eax,(%rax)
  40025e:	00 00                	add    %al,(%rax)
  400260:	47                   	rex.RXB
  400261:	4e 55                	rex.WRX push %rbp
  400263:	00 00                	add    %al,(%rax)
  400265:	00 00                	add    %al,(%rax)
  400267:	00 02                	add    %al,(%rdx)
  400269:	00 00                	add    %al,(%rax)
  40026b:	00 06                	add    %al,(%rsi)
  40026d:	00 00                	add    %al,(%rax)
  40026f:	00 18                	add    %bl,(%rax)
  400271:	00 00                	add    %al,(%rax)
	...

Disassembly of section .note.gnu.build-id:

0000000000400274 <.note.gnu.build-id>:
  400274:	04 00                	add    $0x0,%al
  400276:	00 00                	add    %al,(%rax)
  400278:	14 00                	adc    $0x0,%al
  40027a:	00 00                	add    %al,(%rax)
  40027c:	03 00                	add    (%rax),%eax
  40027e:	00 00                	add    %al,(%rax)
  400280:	47                   	rex.RXB
  400281:	4e 55                	rex.WRX push %rbp
  400283:	00 f4                	add    %dh,%ah
  400285:	0d 0c b6 52 f0       	or     $0xf052b60c,%eax
  40028a:	8a 25 df 2e 72 10    	mov    0x10722edf(%rip),%ah        # 10b2316f <_end+0x10522127>
  400290:	93                   	xchg   %eax,%ebx
  400291:	8d                   	(bad)  
  400292:	f7                   	(bad)  
  400293:	4e d1 41 21          	rex.WRX rolq 0x21(%rcx)
  400297:	70                   	.byte 0x70

Disassembly of section .gnu.hash:

0000000000400298 <.gnu.hash>:
  400298:	01 00                	add    %eax,(%rax)
  40029a:	00 00                	add    %al,(%rax)
  40029c:	01 00                	add    %eax,(%rax)
  40029e:	00 00                	add    %al,(%rax)
  4002a0:	01 00                	add    %eax,(%rax)
	...

Disassembly of section .dynsym:

00000000004002b8 <.dynsym>:
	...
  4002d0:	0b 00                	or     (%rax),%eax
  4002d2:	00 00                	add    %al,(%rax)
  4002d4:	12 00                	adc    (%rax),%al
	...
  4002e6:	00 00                	add    %al,(%rax)
  4002e8:	10 00                	adc    %al,(%rax)
  4002ea:	00 00                	add    %al,(%rax)
  4002ec:	12 00                	adc    (%rax),%al
	...
  4002fe:	00 00                	add    %al,(%rax)
  400300:	22 00                	and    (%rax),%al
  400302:	00 00                	add    %al,(%rax)
  400304:	20 00                	and    %al,(%rax)
	...

Disassembly of section .dynstr:

0000000000400318 <.dynstr>:
  400318:	00 6c 69 62          	add    %ch,0x62(%rcx,%rbp,2)
  40031c:	63 2e                	movslq (%rsi),%ebp
  40031e:	73 6f                	jae    40038f <_init-0x51>
  400320:	2e 36 00 70 75       	cs add %dh,%cs:%ss:0x75(%rax)
  400325:	74 73                	je     40039a <_init-0x46>
  400327:	00 5f 5f             	add    %bl,0x5f(%rdi)
  40032a:	6c                   	insb   (%dx),%es:(%rdi)
  40032b:	69 62 63 5f 73 74 61 	imul   $0x6174735f,0x63(%rdx),%esp
  400332:	72 74                	jb     4003a8 <_init-0x38>
  400334:	5f                   	pop    %rdi
  400335:	6d                   	insl   (%dx),%es:(%rdi)
  400336:	61                   	(bad)  
  400337:	69 6e 00 5f 5f 67 6d 	imul   $0x6d675f5f,0x0(%rsi),%ebp
  40033e:	6f                   	outsl  %ds:(%rsi),(%dx)
  40033f:	6e                   	outsb  %ds:(%rsi),(%dx)
  400340:	5f                   	pop    %rdi
  400341:	73 74                	jae    4003b7 <_init-0x29>
  400343:	61                   	(bad)  
  400344:	72 74                	jb     4003ba <_init-0x26>
  400346:	5f                   	pop    %rdi
  400347:	5f                   	pop    %rdi
  400348:	00 47 4c             	add    %al,0x4c(%rdi)
  40034b:	49                   	rex.WB
  40034c:	42                   	rex.X
  40034d:	43 5f                	rex.XB pop %r15
  40034f:	32 2e                	xor    (%rsi),%ch
  400351:	32 2e                	xor    (%rsi),%ch
  400353:	35                   	.byte 0x35
	...

Disassembly of section .gnu.version:

0000000000400356 <.gnu.version>:
  400356:	00 00                	add    %al,(%rax)
  400358:	02 00                	add    (%rax),%al
  40035a:	02 00                	add    (%rax),%al
	...

Disassembly of section .gnu.version_r:

0000000000400360 <.gnu.version_r>:
  400360:	01 00                	add    %eax,(%rax)
  400362:	01 00                	add    %eax,(%rax)
  400364:	01 00                	add    %eax,(%rax)
  400366:	00 00                	add    %al,(%rax)
  400368:	10 00                	adc    %al,(%rax)
  40036a:	00 00                	add    %al,(%rax)
  40036c:	00 00                	add    %al,(%rax)
  40036e:	00 00                	add    %al,(%rax)
  400370:	75 1a                	jne    40038c <_init-0x54>
  400372:	69 09 00 00 02 00    	imul   $0x20000,(%rcx),%ecx
  400378:	31 00                	xor    %eax,(%rax)
  40037a:	00 00                	add    %al,(%rax)
  40037c:	00 00                	add    %al,(%rax)
	...

Disassembly of section .rela.dyn:

0000000000400380 <.rela.dyn>:
  400380:	f8                   	clc    
  400381:	0f 60 00             	punpcklbw (%rax),%mm0
  400384:	00 00                	add    %al,(%rax)
  400386:	00 00                	add    %al,(%rax)
  400388:	06                   	(bad)  
  400389:	00 00                	add    %al,(%rax)
  40038b:	00 03                	add    %al,(%rbx)
	...

Disassembly of section .rela.plt:

0000000000400398 <.rela.plt>:
  400398:	18 10                	sbb    %dl,(%rax)
  40039a:	60                   	(bad)  
  40039b:	00 00                	add    %al,(%rax)
  40039d:	00 00                	add    %al,(%rax)
  40039f:	00 07                	add    %al,(%rdi)
  4003a1:	00 00                	add    %al,(%rax)
  4003a3:	00 01                	add    %al,(%rcx)
	...
  4003ad:	00 00                	add    %al,(%rax)
  4003af:	00 20                	add    %ah,(%rax)
  4003b1:	10 60 00             	adc    %ah,0x0(%rax)
  4003b4:	00 00                	add    %al,(%rax)
  4003b6:	00 00                	add    %al,(%rax)
  4003b8:	07                   	(bad)  
  4003b9:	00 00                	add    %al,(%rax)
  4003bb:	00 02                	add    %al,(%rdx)
	...
  4003c5:	00 00                	add    %al,(%rax)
  4003c7:	00 28                	add    %ch,(%rax)
  4003c9:	10 60 00             	adc    %ah,0x0(%rax)
  4003cc:	00 00                	add    %al,(%rax)
  4003ce:	00 00                	add    %al,(%rax)
  4003d0:	07                   	(bad)  
  4003d1:	00 00                	add    %al,(%rax)
  4003d3:	00 03                	add    %al,(%rbx)
	...

Disassembly of section .init:

00000000004003e0 <_init>:
  4003e0:	48 83 ec 08          	sub    $0x8,%rsp
  4003e4:	48 8b 05 0d 0c 20 00 	mov    0x200c0d(%rip),%rax        # 600ff8 <_DYNAMIC+0x1d0>
  4003eb:	48 85 c0             	test   %rax,%rax
  4003ee:	74 05                	je     4003f5 <_init+0x15>
  4003f0:	e8 3b 00 00 00       	callq  400430 <__gmon_start__@plt>
  4003f5:	48 83 c4 08          	add    $0x8,%rsp
  4003f9:	c3                   	retq   

Disassembly of section .plt:

0000000000400400 <puts@plt-0x10>:
  400400:	ff 35 02 0c 20 00    	pushq  0x200c02(%rip)        # 601008 <_GLOBAL_OFFSET_TABLE_+0x8>
  400406:	ff 25 04 0c 20 00    	jmpq   *0x200c04(%rip)        # 601010 <_GLOBAL_OFFSET_TABLE_+0x10>
  40040c:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000400410 <puts@plt>:
  400410:	ff 25 02 0c 20 00    	jmpq   *0x200c02(%rip)        # 601018 <_GLOBAL_OFFSET_TABLE_+0x18>
  400416:	68 00 00 00 00       	pushq  $0x0
  40041b:	e9 e0 ff ff ff       	jmpq   400400 <_init+0x20>

0000000000400420 <__libc_start_main@plt>:
  400420:	ff 25 fa 0b 20 00    	jmpq   *0x200bfa(%rip)        # 601020 <_GLOBAL_OFFSET_TABLE_+0x20>
  400426:	68 01 00 00 00       	pushq  $0x1
  40042b:	e9 d0 ff ff ff       	jmpq   400400 <_init+0x20>

0000000000400430 <__gmon_start__@plt>:
  400430:	ff 25 f2 0b 20 00    	jmpq   *0x200bf2(%rip)        # 601028 <_GLOBAL_OFFSET_TABLE_+0x28>
  400436:	68 02 00 00 00       	pushq  $0x2
  40043b:	e9 c0 ff ff ff       	jmpq   400400 <_init+0x20>

Disassembly of section .text:

0000000000400440 <_start>:
```

####Observation

1. When looking at the *entry point* information in [readelf -h hello](readelf_-h_hello.md), this is the
point in the program where the execution kicks off.  It's pretty obvious, based on it's name `start`, but 
sometimes that information may not be available.

```
  400440:	31 ed                	xor    %ebp,%ebp
  400442:	49 89 d1             	mov    %rdx,%r9
  400445:	5e                   	pop    %rsi
  400446:	48 89 e2             	mov    %rsp,%rdx
  400449:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
  40044d:	50                   	push   %rax
  40044e:	54                   	push   %rsp
  40044f:	49 c7 c0 b0 05 40 00 	mov    $0x4005b0,%r8
  400456:	48 c7 c1 40 05 40 00 	mov    $0x400540,%rcx
  40045d:	48 c7 c7 2d 05 40 00 	mov    $0x40052d,%rdi
  400464:	e8 b7 ff ff ff       	callq  400420 <__libc_start_main@plt>
  400469:	f4                   	hlt    
  40046a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

0000000000400470 <deregister_tm_clones>:
  400470:	b8 47 10 60 00       	mov    $0x601047,%eax
  400475:	55                   	push   %rbp
  400476:	48 2d 40 10 60 00    	sub    $0x601040,%rax
  40047c:	48 83 f8 0e          	cmp    $0xe,%rax
  400480:	48 89 e5             	mov    %rsp,%rbp
  400483:	77 02                	ja     400487 <deregister_tm_clones+0x17>
  400485:	5d                   	pop    %rbp
  400486:	c3                   	retq   
  400487:	b8 00 00 00 00       	mov    $0x0,%eax
  40048c:	48 85 c0             	test   %rax,%rax
  40048f:	74 f4                	je     400485 <deregister_tm_clones+0x15>
  400491:	5d                   	pop    %rbp
  400492:	bf 40 10 60 00       	mov    $0x601040,%edi
  400497:	ff e0                	jmpq   *%rax
  400499:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000004004a0 <register_tm_clones>:
  4004a0:	b8 40 10 60 00       	mov    $0x601040,%eax
  4004a5:	55                   	push   %rbp
  4004a6:	48 2d 40 10 60 00    	sub    $0x601040,%rax
  4004ac:	48 c1 f8 03          	sar    $0x3,%rax
  4004b0:	48 89 e5             	mov    %rsp,%rbp
  4004b3:	48 89 c2             	mov    %rax,%rdx
  4004b6:	48 c1 ea 3f          	shr    $0x3f,%rdx
  4004ba:	48 01 d0             	add    %rdx,%rax
  4004bd:	48 d1 f8             	sar    %rax
  4004c0:	75 02                	jne    4004c4 <register_tm_clones+0x24>
  4004c2:	5d                   	pop    %rbp
  4004c3:	c3                   	retq   
  4004c4:	ba 00 00 00 00       	mov    $0x0,%edx
  4004c9:	48 85 d2             	test   %rdx,%rdx
  4004cc:	74 f4                	je     4004c2 <register_tm_clones+0x22>
  4004ce:	5d                   	pop    %rbp
  4004cf:	48 89 c6             	mov    %rax,%rsi
  4004d2:	bf 40 10 60 00       	mov    $0x601040,%edi
  4004d7:	ff e2                	jmpq   *%rdx
  4004d9:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000004004e0 <__do_global_dtors_aux>:
  4004e0:	80 3d 59 0b 20 00 00 	cmpb   $0x0,0x200b59(%rip)        # 601040 <__TMC_END__>
  4004e7:	75 11                	jne    4004fa <__do_global_dtors_aux+0x1a>
  4004e9:	55                   	push   %rbp
  4004ea:	48 89 e5             	mov    %rsp,%rbp
  4004ed:	e8 7e ff ff ff       	callq  400470 <deregister_tm_clones>
  4004f2:	5d                   	pop    %rbp
  4004f3:	c6 05 46 0b 20 00 01 	movb   $0x1,0x200b46(%rip)        # 601040 <__TMC_END__>
  4004fa:	f3 c3                	repz retq 
  4004fc:	0f 1f 40 00          	nopl   0x0(%rax)

0000000000400500 <frame_dummy>:
  400500:	48 83 3d 18 09 20 00 	cmpq   $0x0,0x200918(%rip)        # 600e20 <__JCR_END__>
  400507:	00 
  400508:	74 1e                	je     400528 <frame_dummy+0x28>
  40050a:	b8 00 00 00 00       	mov    $0x0,%eax
  40050f:	48 85 c0             	test   %rax,%rax
  400512:	74 14                	je     400528 <frame_dummy+0x28>
  400514:	55                   	push   %rbp
  400515:	bf 20 0e 60 00       	mov    $0x600e20,%edi
  40051a:	48 89 e5             	mov    %rsp,%rbp
  40051d:	ff d0                	callq  *%rax
  40051f:	5d                   	pop    %rbp
  400520:	e9 7b ff ff ff       	jmpq   4004a0 <register_tm_clones>
  400525:	0f 1f 00             	nopl   (%rax)
  400528:	e9 73 ff ff ff       	jmpq   4004a0 <register_tm_clones>

000000000040052d <main>:
  40052d:	55                   	push   %rbp
  40052e:	48 89 e5             	mov    %rsp,%rbp
  400531:	bf c4 05 40 00       	mov    $0x4005c4,%edi
  400536:	e8 d5 fe ff ff       	callq  400410 <puts@plt>
  40053b:	5d                   	pop    %rbp
  40053c:	c3                   	retq   
  40053d:	0f 1f 00             	nopl   (%rax)

0000000000400540 <__libc_csu_init>:
  400540:	41 57                	push   %r15
  400542:	41 89 ff             	mov    %edi,%r15d
  400545:	41 56                	push   %r14
  400547:	49 89 f6             	mov    %rsi,%r14
  40054a:	41 55                	push   %r13
  40054c:	49 89 d5             	mov    %rdx,%r13
  40054f:	41 54                	push   %r12
  400551:	4c 8d 25 b8 08 20 00 	lea    0x2008b8(%rip),%r12        # 600e10 <__frame_dummy_init_array_entry>
  400558:	55                   	push   %rbp
  400559:	48 8d 2d b8 08 20 00 	lea    0x2008b8(%rip),%rbp        # 600e18 <__init_array_end>
  400560:	53                   	push   %rbx
  400561:	4c 29 e5             	sub    %r12,%rbp
  400564:	31 db                	xor    %ebx,%ebx
  400566:	48 c1 fd 03          	sar    $0x3,%rbp
  40056a:	48 83 ec 08          	sub    $0x8,%rsp
  40056e:	e8 6d fe ff ff       	callq  4003e0 <_init>
  400573:	48 85 ed             	test   %rbp,%rbp
  400576:	74 1e                	je     400596 <__libc_csu_init+0x56>
  400578:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  40057f:	00 
  400580:	4c 89 ea             	mov    %r13,%rdx
  400583:	4c 89 f6             	mov    %r14,%rsi
  400586:	44 89 ff             	mov    %r15d,%edi
  400589:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
  40058d:	48 83 c3 01          	add    $0x1,%rbx
  400591:	48 39 eb             	cmp    %rbp,%rbx
  400594:	75 ea                	jne    400580 <__libc_csu_init+0x40>
  400596:	48 83 c4 08          	add    $0x8,%rsp
  40059a:	5b                   	pop    %rbx
  40059b:	5d                   	pop    %rbp
  40059c:	41 5c                	pop    %r12
  40059e:	41 5d                	pop    %r13
  4005a0:	41 5e                	pop    %r14
  4005a2:	41 5f                	pop    %r15
  4005a4:	c3                   	retq   
  4005a5:	66 66 2e 0f 1f 84 00 	data32 nopw %cs:0x0(%rax,%rax,1)
  4005ac:	00 00 00 00 

00000000004005b0 <__libc_csu_fini>:
  4005b0:	f3 c3                	repz retq 

Disassembly of section .fini:

00000000004005b4 <_fini>:
  4005b4:	48 83 ec 08          	sub    $0x8,%rsp
  4005b8:	48 83 c4 08          	add    $0x8,%rsp
  4005bc:	c3                   	retq   

Disassembly of section .rodata:

00000000004005c0 <_IO_stdin_used>:
  4005c0:	01 00                	add    %eax,(%rax)
  4005c2:	02 00                	add    (%rax),%al
  4005c4:	48                   	rex.W
  4005c5:	65                   	gs
  4005c6:	6c                   	insb   (%dx),%es:(%rdi)
  4005c7:	6c                   	insb   (%dx),%es:(%rdi)
  4005c8:	6f                   	outsl  %ds:(%rsi),(%dx)
  4005c9:	20 57 6f             	and    %dl,0x6f(%rdi)
  4005cc:	72 6c                	jb     40063a <_IO_stdin_used+0x7a>
  4005ce:	64 21 00             	and    %eax,%fs:(%rax)

Disassembly of section .eh_frame_hdr:

00000000004005d4 <.eh_frame_hdr>:
  4005d4:	01 1b                	add    %ebx,(%rbx)
  4005d6:	03 3b                	add    (%rbx),%edi
  4005d8:	30 00                	xor    %al,(%rax)
  4005da:	00 00                	add    %al,(%rax)
  4005dc:	05 00 00 00 2c       	add    $0x2c000000,%eax
  4005e1:	fe                   	(bad)  
  4005e2:	ff                   	(bad)  
  4005e3:	ff                   	(bad)  
  4005e4:	7c 00                	jl     4005e6 <_IO_stdin_used+0x26>
  4005e6:	00 00                	add    %al,(%rax)
  4005e8:	6c                   	insb   (%dx),%es:(%rdi)
  4005e9:	fe                   	(bad)  
  4005ea:	ff                   	(bad)  
  4005eb:	ff 4c 00 00          	decl   0x0(%rax,%rax,1)
  4005ef:	00 59 ff             	add    %bl,-0x1(%rcx)
  4005f2:	ff                   	(bad)  
  4005f3:	ff a4 00 00 00 6c ff 	jmpq   *-0x940000(%rax,%rax,1)
  4005fa:	ff                   	(bad)  
  4005fb:	ff c4                	inc    %esp
  4005fd:	00 00                	add    %al,(%rax)
  4005ff:	00 dc                	add    %bl,%ah
  400601:	ff                   	(bad)  
  400602:	ff                   	(bad)  
  400603:	ff 0c 01             	decl   (%rcx,%rax,1)
	...

Disassembly of section .eh_frame:

0000000000400608 <__FRAME_END__-0xf0>:
  400608:	14 00                	adc    $0x0,%al
  40060a:	00 00                	add    %al,(%rax)
  40060c:	00 00                	add    %al,(%rax)
  40060e:	00 00                	add    %al,(%rax)
  400610:	01 7a 52             	add    %edi,0x52(%rdx)
  400613:	00 01                	add    %al,(%rcx)
  400615:	78 10                	js     400627 <_IO_stdin_used+0x67>
  400617:	01 1b                	add    %ebx,(%rbx)
  400619:	0c 07                	or     $0x7,%al
  40061b:	08 90 01 07 10 14    	or     %dl,0x14100701(%rax)
  400621:	00 00                	add    %al,(%rax)
  400623:	00 1c 00             	add    %bl,(%rax,%rax,1)
  400626:	00 00                	add    %al,(%rax)
  400628:	18 fe                	sbb    %bh,%dh
  40062a:	ff                   	(bad)  
  40062b:	ff 2a                	ljmpq  *(%rdx)
	...
  400635:	00 00                	add    %al,(%rax)
  400637:	00 14 00             	add    %dl,(%rax,%rax,1)
  40063a:	00 00                	add    %al,(%rax)
  40063c:	00 00                	add    %al,(%rax)
  40063e:	00 00                	add    %al,(%rax)
  400640:	01 7a 52             	add    %edi,0x52(%rdx)
  400643:	00 01                	add    %al,(%rcx)
  400645:	78 10                	js     400657 <_IO_stdin_used+0x97>
  400647:	01 1b                	add    %ebx,(%rbx)
  400649:	0c 07                	or     $0x7,%al
  40064b:	08 90 01 00 00 24    	or     %dl,0x24000001(%rax)
  400651:	00 00                	add    %al,(%rax)
  400653:	00 1c 00             	add    %bl,(%rax,%rax,1)
  400656:	00 00                	add    %al,(%rax)
  400658:	a8 fd                	test   $0xfd,%al
  40065a:	ff                   	(bad)  
  40065b:	ff 40 00             	incl   0x0(%rax)
  40065e:	00 00                	add    %al,(%rax)
  400660:	00 0e                	add    %cl,(%rsi)
  400662:	10 46 0e             	adc    %al,0xe(%rsi)
  400665:	18 4a 0f             	sbb    %cl,0xf(%rdx)
  400668:	0b 77 08             	or     0x8(%rdi),%esi
  40066b:	80 00 3f             	addb   $0x3f,(%rax)
  40066e:	1a 3b                	sbb    (%rbx),%bh
  400670:	2a 33                	sub    (%rbx),%dh
  400672:	24 22                	and    $0x22,%al
  400674:	00 00                	add    %al,(%rax)
  400676:	00 00                	add    %al,(%rax)
  400678:	1c 00                	sbb    $0x0,%al
  40067a:	00 00                	add    %al,(%rax)
  40067c:	44 00 00             	add    %r8b,(%rax)
  40067f:	00 ad fe ff ff 10    	add    %ch,0x10fffffe(%rbp)
  400685:	00 00                	add    %al,(%rax)
  400687:	00 00                	add    %al,(%rax)
  400689:	41 0e                	rex.B (bad) 
  40068b:	10 86 02 43 0d 06    	adc    %al,0x60d4302(%rsi)
  400691:	4b 0c 07             	rex.WXB or $0x7,%al
  400694:	08 00                	or     %al,(%rax)
  400696:	00 00                	add    %al,(%rax)
  400698:	44 00 00             	add    %r8b,(%rax)
  40069b:	00 64 00 00          	add    %ah,0x0(%rax,%rax,1)
  40069f:	00 a0 fe ff ff 65    	add    %ah,0x65fffffe(%rax)
  4006a5:	00 00                	add    %al,(%rax)
  4006a7:	00 00                	add    %al,(%rax)
  4006a9:	42 0e                	rex.X (bad) 
  4006ab:	10 8f 02 45 0e 18    	adc    %cl,0x180e4502(%rdi)
  4006b1:	8e 03                	mov    (%rbx),%es
  4006b3:	45 0e                	rex.RB (bad) 
  4006b5:	20 8d 04 45 0e 28    	and    %cl,0x280e4504(%rbp)
  4006bb:	8c 05 48 0e 30 86    	mov    %es,-0x79cff1b8(%rip)        # ffffffff86701509 <_end+0xffffffff861004c1>
  4006c1:	06                   	(bad)  
  4006c2:	48 0e                	rex.W (bad) 
  4006c4:	38 83 07 4d 0e 40    	cmp    %al,0x400e4d07(%rbx)
  4006ca:	6c                   	insb   (%dx),%es:(%rdi)
  4006cb:	0e                   	(bad)  
  4006cc:	38 41 0e             	cmp    %al,0xe(%rcx)
  4006cf:	30 41 0e             	xor    %al,0xe(%rcx)
  4006d2:	28 42 0e             	sub    %al,0xe(%rdx)
  4006d5:	20 42 0e             	and    %al,0xe(%rdx)
  4006d8:	18 42 0e             	sbb    %al,0xe(%rdx)
  4006db:	10 42 0e             	adc    %al,0xe(%rdx)
  4006de:	08 00                	or     %al,(%rax)
  4006e0:	14 00                	adc    $0x0,%al
  4006e2:	00 00                	add    %al,(%rax)
  4006e4:	ac                   	lods   %ds:(%rsi),%al
  4006e5:	00 00                	add    %al,(%rax)
  4006e7:	00 c8                	add    %cl,%al
  4006e9:	fe                   	(bad)  
  4006ea:	ff                   	(bad)  
  4006eb:	ff 02                	incl   (%rdx)
	...

00000000004006f8 <__FRAME_END__>:
  4006f8:	00 00                	add    %al,(%rax)
	...

Disassembly of section .init_array:

0000000000600e10 <__frame_dummy_init_array_entry>:
  600e10:	00 05 40 00 00 00    	add    %al,0x40(%rip)        # 600e56 <_DYNAMIC+0x2e>
	...

Disassembly of section .fini_array:

0000000000600e18 <__do_global_dtors_aux_fini_array_entry>:
  600e18:	e0 04                	loopne 600e1e <__do_global_dtors_aux_fini_array_entry+0x6>
  600e1a:	40 00 00             	add    %al,(%rax)
  600e1d:	00 00                	add    %al,(%rax)
	...

Disassembly of section .jcr:

0000000000600e20 <__JCR_END__>:
	...

Disassembly of section .dynamic:

0000000000600e28 <_DYNAMIC>:
  600e28:	01 00                	add    %eax,(%rax)
  600e2a:	00 00                	add    %al,(%rax)
  600e2c:	00 00                	add    %al,(%rax)
  600e2e:	00 00                	add    %al,(%rax)
  600e30:	01 00                	add    %eax,(%rax)
  600e32:	00 00                	add    %al,(%rax)
  600e34:	00 00                	add    %al,(%rax)
  600e36:	00 00                	add    %al,(%rax)
  600e38:	0c 00                	or     $0x0,%al
  600e3a:	00 00                	add    %al,(%rax)
  600e3c:	00 00                	add    %al,(%rax)
  600e3e:	00 00                	add    %al,(%rax)
  600e40:	e0 03                	loopne 600e45 <_DYNAMIC+0x1d>
  600e42:	40 00 00             	add    %al,(%rax)
  600e45:	00 00                	add    %al,(%rax)
  600e47:	00 0d 00 00 00 00    	add    %cl,0x0(%rip)        # 600e4d <_DYNAMIC+0x25>
  600e4d:	00 00                	add    %al,(%rax)
  600e4f:	00 b4 05 40 00 00 00 	add    %dh,0x40(%rbp,%rax,1)
  600e56:	00 00                	add    %al,(%rax)
  600e58:	19 00                	sbb    %eax,(%rax)
  600e5a:	00 00                	add    %al,(%rax)
  600e5c:	00 00                	add    %al,(%rax)
  600e5e:	00 00                	add    %al,(%rax)
  600e60:	10 0e                	adc    %cl,(%rsi)
  600e62:	60                   	(bad)  
  600e63:	00 00                	add    %al,(%rax)
  600e65:	00 00                	add    %al,(%rax)
  600e67:	00 1b                	add    %bl,(%rbx)
  600e69:	00 00                	add    %al,(%rax)
  600e6b:	00 00                	add    %al,(%rax)
  600e6d:	00 00                	add    %al,(%rax)
  600e6f:	00 08                	add    %cl,(%rax)
  600e71:	00 00                	add    %al,(%rax)
  600e73:	00 00                	add    %al,(%rax)
  600e75:	00 00                	add    %al,(%rax)
  600e77:	00 1a                	add    %bl,(%rdx)
  600e79:	00 00                	add    %al,(%rax)
  600e7b:	00 00                	add    %al,(%rax)
  600e7d:	00 00                	add    %al,(%rax)
  600e7f:	00 18                	add    %bl,(%rax)
  600e81:	0e                   	(bad)  
  600e82:	60                   	(bad)  
  600e83:	00 00                	add    %al,(%rax)
  600e85:	00 00                	add    %al,(%rax)
  600e87:	00 1c 00             	add    %bl,(%rax,%rax,1)
  600e8a:	00 00                	add    %al,(%rax)
  600e8c:	00 00                	add    %al,(%rax)
  600e8e:	00 00                	add    %al,(%rax)
  600e90:	08 00                	or     %al,(%rax)
  600e92:	00 00                	add    %al,(%rax)
  600e94:	00 00                	add    %al,(%rax)
  600e96:	00 00                	add    %al,(%rax)
  600e98:	f5                   	cmc    
  600e99:	fe                   	(bad)  
  600e9a:	ff 6f 00             	ljmpq  *0x0(%rdi)
  600e9d:	00 00                	add    %al,(%rax)
  600e9f:	00 98 02 40 00 00    	add    %bl,0x4002(%rax)
  600ea5:	00 00                	add    %al,(%rax)
  600ea7:	00 05 00 00 00 00    	add    %al,0x0(%rip)        # 600ead <_DYNAMIC+0x85>
  600ead:	00 00                	add    %al,(%rax)
  600eaf:	00 18                	add    %bl,(%rax)
  600eb1:	03 40 00             	add    0x0(%rax),%eax
  600eb4:	00 00                	add    %al,(%rax)
  600eb6:	00 00                	add    %al,(%rax)
  600eb8:	06                   	(bad)  
  600eb9:	00 00                	add    %al,(%rax)
  600ebb:	00 00                	add    %al,(%rax)
  600ebd:	00 00                	add    %al,(%rax)
  600ebf:	00 b8 02 40 00 00    	add    %bh,0x4002(%rax)
  600ec5:	00 00                	add    %al,(%rax)
  600ec7:	00 0a                	add    %cl,(%rdx)
  600ec9:	00 00                	add    %al,(%rax)
  600ecb:	00 00                	add    %al,(%rax)
  600ecd:	00 00                	add    %al,(%rax)
  600ecf:	00 3d 00 00 00 00    	add    %bh,0x0(%rip)        # 600ed5 <_DYNAMIC+0xad>
  600ed5:	00 00                	add    %al,(%rax)
  600ed7:	00 0b                	add    %cl,(%rbx)
  600ed9:	00 00                	add    %al,(%rax)
  600edb:	00 00                	add    %al,(%rax)
  600edd:	00 00                	add    %al,(%rax)
  600edf:	00 18                	add    %bl,(%rax)
  600ee1:	00 00                	add    %al,(%rax)
  600ee3:	00 00                	add    %al,(%rax)
  600ee5:	00 00                	add    %al,(%rax)
  600ee7:	00 15 00 00 00 00    	add    %dl,0x0(%rip)        # 600eed <_DYNAMIC+0xc5>
	...
  600ef5:	00 00                	add    %al,(%rax)
  600ef7:	00 03                	add    %al,(%rbx)
	...
  600f01:	10 60 00             	adc    %ah,0x0(%rax)
  600f04:	00 00                	add    %al,(%rax)
  600f06:	00 00                	add    %al,(%rax)
  600f08:	02 00                	add    (%rax),%al
  600f0a:	00 00                	add    %al,(%rax)
  600f0c:	00 00                	add    %al,(%rax)
  600f0e:	00 00                	add    %al,(%rax)
  600f10:	48 00 00             	rex.W add %al,(%rax)
  600f13:	00 00                	add    %al,(%rax)
  600f15:	00 00                	add    %al,(%rax)
  600f17:	00 14 00             	add    %dl,(%rax,%rax,1)
  600f1a:	00 00                	add    %al,(%rax)
  600f1c:	00 00                	add    %al,(%rax)
  600f1e:	00 00                	add    %al,(%rax)
  600f20:	07                   	(bad)  
  600f21:	00 00                	add    %al,(%rax)
  600f23:	00 00                	add    %al,(%rax)
  600f25:	00 00                	add    %al,(%rax)
  600f27:	00 17                	add    %dl,(%rdi)
  600f29:	00 00                	add    %al,(%rax)
  600f2b:	00 00                	add    %al,(%rax)
  600f2d:	00 00                	add    %al,(%rax)
  600f2f:	00 98 03 40 00 00    	add    %bl,0x4003(%rax)
  600f35:	00 00                	add    %al,(%rax)
  600f37:	00 07                	add    %al,(%rdi)
  600f39:	00 00                	add    %al,(%rax)
  600f3b:	00 00                	add    %al,(%rax)
  600f3d:	00 00                	add    %al,(%rax)
  600f3f:	00 80 03 40 00 00    	add    %al,0x4003(%rax)
  600f45:	00 00                	add    %al,(%rax)
  600f47:	00 08                	add    %cl,(%rax)
  600f49:	00 00                	add    %al,(%rax)
  600f4b:	00 00                	add    %al,(%rax)
  600f4d:	00 00                	add    %al,(%rax)
  600f4f:	00 18                	add    %bl,(%rax)
  600f51:	00 00                	add    %al,(%rax)
  600f53:	00 00                	add    %al,(%rax)
  600f55:	00 00                	add    %al,(%rax)
  600f57:	00 09                	add    %cl,(%rcx)
  600f59:	00 00                	add    %al,(%rax)
  600f5b:	00 00                	add    %al,(%rax)
  600f5d:	00 00                	add    %al,(%rax)
  600f5f:	00 18                	add    %bl,(%rax)
  600f61:	00 00                	add    %al,(%rax)
  600f63:	00 00                	add    %al,(%rax)
  600f65:	00 00                	add    %al,(%rax)
  600f67:	00 fe                	add    %bh,%dh
  600f69:	ff                   	(bad)  
  600f6a:	ff 6f 00             	ljmpq  *0x0(%rdi)
  600f6d:	00 00                	add    %al,(%rax)
  600f6f:	00 60 03             	add    %ah,0x3(%rax)
  600f72:	40 00 00             	add    %al,(%rax)
  600f75:	00 00                	add    %al,(%rax)
  600f77:	00 ff                	add    %bh,%bh
  600f79:	ff                   	(bad)  
  600f7a:	ff 6f 00             	ljmpq  *0x0(%rdi)
  600f7d:	00 00                	add    %al,(%rax)
  600f7f:	00 01                	add    %al,(%rcx)
  600f81:	00 00                	add    %al,(%rax)
  600f83:	00 00                	add    %al,(%rax)
  600f85:	00 00                	add    %al,(%rax)
  600f87:	00 f0                	add    %dh,%al
  600f89:	ff                   	(bad)  
  600f8a:	ff 6f 00             	ljmpq  *0x0(%rdi)
  600f8d:	00 00                	add    %al,(%rax)
  600f8f:	00 56 03             	add    %dl,0x3(%rsi)
  600f92:	40 00 00             	add    %al,(%rax)
	...

Disassembly of section .got:

0000000000600ff8 <.got>:
	...

Disassembly of section .got.plt:

0000000000601000 <_GLOBAL_OFFSET_TABLE_>:
  601000:	28 0e                	sub    %cl,(%rsi)
  601002:	60                   	(bad)  
	...
  601017:	00 16                	add    %dl,(%rsi)
  601019:	04 40                	add    $0x40,%al
  60101b:	00 00                	add    %al,(%rax)
  60101d:	00 00                	add    %al,(%rax)
  60101f:	00 26                	add    %ah,(%rsi)
  601021:	04 40                	add    $0x40,%al
  601023:	00 00                	add    %al,(%rax)
  601025:	00 00                	add    %al,(%rax)
  601027:	00 36                	add    %dh,(%rsi)
  601029:	04 40                	add    $0x40,%al
  60102b:	00 00                	add    %al,(%rax)
  60102d:	00 00                	add    %al,(%rax)
	...

Disassembly of section .data:

0000000000601030 <__data_start>:
	...

0000000000601038 <__dso_handle>:
	...

Disassembly of section .bss:

0000000000601040 <__bss_start>:
	...

Disassembly of section .comment:

0000000000000000 <.comment>:
   0:	47                   	rex.RXB
   1:	43                   	rex.XB
   2:	43 3a 20             	rex.XB cmp (%r8),%spl
   5:	28 55 62             	sub    %dl,0x62(%rbp)
   8:	75 6e                	jne    78 <_init-0x400368>
   a:	74 75                	je     81 <_init-0x40035f>
   c:	20 34 2e             	and    %dh,(%rsi,%rbp,1)
   f:	38 2e                	cmp    %ch,(%rsi)
  11:	34 2d                	xor    $0x2d,%al
  13:	32 75 62             	xor    0x62(%rbp),%dh
  16:	75 6e                	jne    86 <_init-0x40035a>
  18:	74 75                	je     8f <_init-0x400351>
  1a:	31 7e 31             	xor    %edi,0x31(%rsi)
  1d:	34 2e                	xor    $0x2e,%al
  1f:	30 34 29             	xor    %dh,(%rcx,%rbp,1)
  22:	20 34 2e             	and    %dh,(%rsi,%rbp,1)
  25:	38 2e                	cmp    %ch,(%rsi)
  27:	34 00                	xor    $0x0,%al
  29:	47                   	rex.RXB
  2a:	43                   	rex.XB
  2b:	43 3a 20             	rex.XB cmp (%r8),%spl
  2e:	28 55 62             	sub    %dl,0x62(%rbp)
  31:	75 6e                	jne    a1 <_init-0x40033f>
  33:	74 75                	je     aa <_init-0x400336>
  35:	20 34 2e             	and    %dh,(%rsi,%rbp,1)
  38:	38 2e                	cmp    %ch,(%rsi)
  3a:	32 2d 31 39 75 62    	xor    0x62753931(%rip),%ch        # 62753971 <_end+0x62152929>
  40:	75 6e                	jne    b0 <_init-0x400330>
  42:	74 75                	je     b9 <_init-0x400327>
  44:	31 29                	xor    %ebp,(%rcx)
  46:	20 34 2e             	and    %dh,(%rsi,%rbp,1)
  49:	38 2e                	cmp    %ch,(%rsi)
  4b:	32 00                	xor    (%rax),%al``

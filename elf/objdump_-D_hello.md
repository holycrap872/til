# Objdump Breakdown

When I ran `objdump -D hello`, I got the following output.  I intersperse
my comments with references to [readelf -l hello](readelf_-l_hello.md) and
[readelf -h hello](readelf_-h_hello.md).

```
test:     file format elf64-x86-64


Disassembly of section .interp:

0000000000400238 <.interp>:
  400238:	2f                   	(bad)  
  400239:	6c                   	insb   (%dx),%es:(%rdi)
  40023a:	69 62 36 34 2f 6c 64 	imul   $0x646c2f34,0x36(%rdx),%esp
  400241:	2d 6c 69 6e 75       	sub    $0x756e696c,%eax
  400246:	78 2d                	js     400275 <_init-0x133>
  400248:	78 38                	js     400282 <_init-0x126>
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
  400283:	00 d8                	add    %bl,%al
  400285:	83 4c 32 f2 6e       	orl    $0x6e,-0xe(%rdx,%rsi,1)
  40028a:	c0 3a e1             	sarb   $0xe1,(%rdx)
  40028d:	fb                   	sti    
  40028e:	6c                   	insb   (%dx),%es:(%rdi)
  40028f:	cb                   	lret   
  400290:	0d 83 00 27 6c       	or     $0x6c270083,%eax
  400295:	77 97                	ja     40022e <_init-0x17a>
  400297:	32                   	.byte 0x32

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
  4002e8:	1d 00 00 00 20       	sbb    $0x20000000,%eax
	...

Disassembly of section .dynstr:

0000000000400300 <.dynstr>:
  400300:	00 6c 69 62          	add    %ch,0x62(%rcx,%rbp,2)
  400304:	63 2e                	movslq (%rsi),%ebp
  400306:	73 6f                	jae    400377 <_init-0x31>
  400308:	2e 36 00 5f 5f       	cs add %bl,%cs:%ss:0x5f(%rdi)
  40030d:	6c                   	insb   (%dx),%es:(%rdi)
  40030e:	69 62 63 5f 73 74 61 	imul   $0x6174735f,0x63(%rdx),%esp
  400315:	72 74                	jb     40038b <_init-0x1d>
  400317:	5f                   	pop    %rdi
  400318:	6d                   	insl   (%dx),%es:(%rdi)
  400319:	61                   	(bad)  
  40031a:	69 6e 00 5f 5f 67 6d 	imul   $0x6d675f5f,0x0(%rsi),%ebp
  400321:	6f                   	outsl  %ds:(%rsi),(%dx)
  400322:	6e                   	outsb  %ds:(%rsi),(%dx)
  400323:	5f                   	pop    %rdi
  400324:	73 74                	jae    40039a <_init-0xe>
  400326:	61                   	(bad)  
  400327:	72 74                	jb     40039d <_init-0xb>
  400329:	5f                   	pop    %rdi
  40032a:	5f                   	pop    %rdi
  40032b:	00 47 4c             	add    %al,0x4c(%rdi)
  40032e:	49                   	rex.WB
  40032f:	42                   	rex.X
  400330:	43 5f                	rex.XB pop %r15
  400332:	32 2e                	xor    (%rsi),%ch
  400334:	32 2e                	xor    (%rsi),%ch
  400336:	35                   	.byte 0x35
	...

Disassembly of section .gnu.version:

0000000000400338 <.gnu.version>:
  400338:	00 00                	add    %al,(%rax)
  40033a:	02 00                	add    (%rax),%al
	...

Disassembly of section .gnu.version_r:

0000000000400340 <.gnu.version_r>:
  400340:	01 00                	add    %eax,(%rax)
  400342:	01 00                	add    %eax,(%rax)
  400344:	01 00                	add    %eax,(%rax)
  400346:	00 00                	add    %al,(%rax)
  400348:	10 00                	adc    %al,(%rax)
  40034a:	00 00                	add    %al,(%rax)
  40034c:	00 00                	add    %al,(%rax)
  40034e:	00 00                	add    %al,(%rax)
  400350:	75 1a                	jne    40036c <_init-0x3c>
  400352:	69 09 00 00 02 00    	imul   $0x20000,(%rcx),%ecx
  400358:	2c 00                	sub    $0x0,%al
  40035a:	00 00                	add    %al,(%rax)
  40035c:	00 00                	add    %al,(%rax)
	...

Disassembly of section .rela.dyn:

0000000000400360 <.rela.dyn>:
  400360:	f8                   	clc    
  400361:	0f 60 00             	punpcklbw (%rax),%mm0
  400364:	00 00                	add    %al,(%rax)
  400366:	00 00                	add    %al,(%rax)
  400368:	06                   	(bad)  
  400369:	00 00                	add    %al,(%rax)
  40036b:	00 02                	add    %al,(%rdx)
	...

Disassembly of section .rela.plt:

0000000000400378 <.rela.plt>:
  400378:	18 10                	sbb    %dl,(%rax)
  40037a:	60                   	(bad)  
  40037b:	00 00                	add    %al,(%rax)
  40037d:	00 00                	add    %al,(%rax)
  40037f:	00 07                	add    %al,(%rdi)
  400381:	00 00                	add    %al,(%rax)
  400383:	00 01                	add    %al,(%rcx)
	...
  40038d:	00 00                	add    %al,(%rax)
  40038f:	00 20                	add    %ah,(%rax)
  400391:	10 60 00             	adc    %ah,0x0(%rax)
  400394:	00 00                	add    %al,(%rax)
  400396:	00 00                	add    %al,(%rax)
  400398:	07                   	(bad)  
  400399:	00 00                	add    %al,(%rax)
  40039b:	00 02                	add    %al,(%rdx)
	...

Disassembly of section .init:

00000000004003a8 <_init>:
  4003a8:	48 83 ec 08          	sub    $0x8,%rsp
  4003ac:	48 8b 05 45 0c 20 00 	mov    0x200c45(%rip),%rax        # 600ff8 <_DYNAMIC+0x1d0>
  4003b3:	48 85 c0             	test   %rax,%rax
  4003b6:	74 05                	je     4003bd <_init+0x15>
  4003b8:	e8 33 00 00 00       	callq  4003f0 <__gmon_start__@plt>
  4003bd:	48 83 c4 08          	add    $0x8,%rsp
  4003c1:	c3                   	retq   

Disassembly of section .plt:

00000000004003d0 <__libc_start_main@plt-0x10>:
  4003d0:	ff 35 32 0c 20 00    	pushq  0x200c32(%rip)        # 601008 <_GLOBAL_OFFSET_TABLE_+0x8>
  4003d6:	ff 25 34 0c 20 00    	jmpq   *0x200c34(%rip)        # 601010 <_GLOBAL_OFFSET_TABLE_+0x10>
  4003dc:	0f 1f 40 00          	nopl   0x0(%rax)

00000000004003e0 <__libc_start_main@plt>:
  4003e0:	ff 25 32 0c 20 00    	jmpq   *0x200c32(%rip)        # 601018 <_GLOBAL_OFFSET_TABLE_+0x18>
  4003e6:	68 00 00 00 00       	pushq  $0x0
  4003eb:	e9 e0 ff ff ff       	jmpq   4003d0 <_init+0x28>

00000000004003f0 <__gmon_start__@plt>:
  4003f0:	ff 25 2a 0c 20 00    	jmpq   *0x200c2a(%rip)        # 601020 <_GLOBAL_OFFSET_TABLE_+0x20>
  4003f6:	68 01 00 00 00       	pushq  $0x1
  4003fb:	e9 d0 ff ff ff       	jmpq   4003d0 <_init+0x28>

Disassembly of section .text:

0000000000400400 <_start>:
  400400:	31 ed                	xor    %ebp,%ebp
  400402:	49 89 d1             	mov    %rdx,%r9
  400405:	5e                   	pop    %rsi
  400406:	48 89 e2             	mov    %rsp,%rdx
  400409:	48 83 e4 f0          	and    $0xfffffffffffffff0,%rsp
  40040d:	50                   	push   %rax
  40040e:	54                   	push   %rsp
  40040f:	49 c7 c0 a0 05 40 00 	mov    $0x4005a0,%r8
  400416:	48 c7 c1 30 05 40 00 	mov    $0x400530,%rcx
  40041d:	48 c7 c7 08 05 40 00 	mov    $0x400508,%rdi
  400424:	e8 b7 ff ff ff       	callq  4003e0 <__libc_start_main@plt>
  400429:	f4                   	hlt    
  40042a:	66 0f 1f 44 00 00    	nopw   0x0(%rax,%rax,1)

0000000000400430 <deregister_tm_clones>:
  400430:	b8 3f 10 60 00       	mov    $0x60103f,%eax
  400435:	55                   	push   %rbp
  400436:	48 2d 38 10 60 00    	sub    $0x601038,%rax
  40043c:	48 83 f8 0e          	cmp    $0xe,%rax
  400440:	48 89 e5             	mov    %rsp,%rbp
  400443:	77 02                	ja     400447 <deregister_tm_clones+0x17>
  400445:	5d                   	pop    %rbp
  400446:	c3                   	retq   
  400447:	b8 00 00 00 00       	mov    $0x0,%eax
  40044c:	48 85 c0             	test   %rax,%rax
  40044f:	74 f4                	je     400445 <deregister_tm_clones+0x15>
  400451:	5d                   	pop    %rbp
  400452:	bf 38 10 60 00       	mov    $0x601038,%edi
  400457:	ff e0                	jmpq   *%rax
  400459:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

0000000000400460 <register_tm_clones>:
  400460:	b8 38 10 60 00       	mov    $0x601038,%eax
  400465:	55                   	push   %rbp
  400466:	48 2d 38 10 60 00    	sub    $0x601038,%rax
  40046c:	48 c1 f8 03          	sar    $0x3,%rax
  400470:	48 89 e5             	mov    %rsp,%rbp
  400473:	48 89 c2             	mov    %rax,%rdx
  400476:	48 c1 ea 3f          	shr    $0x3f,%rdx
  40047a:	48 01 d0             	add    %rdx,%rax
  40047d:	48 d1 f8             	sar    %rax
  400480:	75 02                	jne    400484 <register_tm_clones+0x24>
  400482:	5d                   	pop    %rbp
  400483:	c3                   	retq   
  400484:	ba 00 00 00 00       	mov    $0x0,%edx
  400489:	48 85 d2             	test   %rdx,%rdx
  40048c:	74 f4                	je     400482 <register_tm_clones+0x22>
  40048e:	5d                   	pop    %rbp
  40048f:	48 89 c6             	mov    %rax,%rsi
  400492:	bf 38 10 60 00       	mov    $0x601038,%edi
  400497:	ff e2                	jmpq   *%rdx
  400499:	0f 1f 80 00 00 00 00 	nopl   0x0(%rax)

00000000004004a0 <__do_global_dtors_aux>:
  4004a0:	80 3d 91 0b 20 00 00 	cmpb   $0x0,0x200b91(%rip)        # 601038 <__TMC_END__>
  4004a7:	75 11                	jne    4004ba <__do_global_dtors_aux+0x1a>
  4004a9:	55                   	push   %rbp
  4004aa:	48 89 e5             	mov    %rsp,%rbp
  4004ad:	e8 7e ff ff ff       	callq  400430 <deregister_tm_clones>
  4004b2:	5d                   	pop    %rbp
  4004b3:	c6 05 7e 0b 20 00 01 	movb   $0x1,0x200b7e(%rip)        # 601038 <__TMC_END__>
  4004ba:	f3 c3                	repz retq 
  4004bc:	0f 1f 40 00          	nopl   0x0(%rax)

00000000004004c0 <frame_dummy>:
  4004c0:	48 83 3d 58 09 20 00 	cmpq   $0x0,0x200958(%rip)        # 600e20 <__JCR_END__>
  4004c7:	00 
  4004c8:	74 1e                	je     4004e8 <frame_dummy+0x28>
  4004ca:	b8 00 00 00 00       	mov    $0x0,%eax
  4004cf:	48 85 c0             	test   %rax,%rax
  4004d2:	74 14                	je     4004e8 <frame_dummy+0x28>
  4004d4:	55                   	push   %rbp
  4004d5:	bf 20 0e 60 00       	mov    $0x600e20,%edi
  4004da:	48 89 e5             	mov    %rsp,%rbp
  4004dd:	ff d0                	callq  *%rax
  4004df:	5d                   	pop    %rbp
  4004e0:	e9 7b ff ff ff       	jmpq   400460 <register_tm_clones>
  4004e5:	0f 1f 00             	nopl   (%rax)
  4004e8:	e9 73 ff ff ff       	jmpq   400460 <register_tm_clones>

00000000004004ed <_Z3reti>:
  4004ed:	55                   	push   %rbp
  4004ee:	48 89 e5             	mov    %rsp,%rbp
  4004f1:	89 7d fc             	mov    %edi,-0x4(%rbp)
  4004f4:	83 7d fc 03          	cmpl   $0x3,-0x4(%rbp)
  4004f8:	75 07                	jne    400501 <_Z3reti+0x14>
  4004fa:	b8 01 00 00 00       	mov    $0x1,%eax
  4004ff:	eb 05                	jmp    400506 <_Z3reti+0x19>
  400501:	b8 00 00 00 00       	mov    $0x0,%eax
  400506:	5d                   	pop    %rbp
  400507:	c3                   	retq   

0000000000400508 <main>:
  400508:	55                   	push   %rbp
  400509:	48 89 e5             	mov    %rsp,%rbp
  40050c:	48 83 ec 10          	sub    $0x10,%rsp
  400510:	89 7d fc             	mov    %edi,-0x4(%rbp)
  400513:	48 89 75 f0          	mov    %rsi,-0x10(%rbp)
  400517:	8b 45 fc             	mov    -0x4(%rbp),%eax
  40051a:	89 c7                	mov    %eax,%edi
  40051c:	e8 cc ff ff ff       	callq  4004ed <_Z3reti>
  400521:	c9                   	leaveq 
  400522:	c3                   	retq   
  400523:	66 2e 0f 1f 84 00 00 	nopw   %cs:0x0(%rax,%rax,1)
  40052a:	00 00 00 
  40052d:	0f 1f 00             	nopl   (%rax)

0000000000400530 <__libc_csu_init>:
  400530:	41 57                	push   %r15
  400532:	41 89 ff             	mov    %edi,%r15d
  400535:	41 56                	push   %r14
  400537:	49 89 f6             	mov    %rsi,%r14
  40053a:	41 55                	push   %r13
  40053c:	49 89 d5             	mov    %rdx,%r13
  40053f:	41 54                	push   %r12
  400541:	4c 8d 25 c8 08 20 00 	lea    0x2008c8(%rip),%r12        # 600e10 <__frame_dummy_init_array_entry>
  400548:	55                   	push   %rbp
  400549:	48 8d 2d c8 08 20 00 	lea    0x2008c8(%rip),%rbp        # 600e18 <__init_array_end>
  400550:	53                   	push   %rbx
  400551:	4c 29 e5             	sub    %r12,%rbp
  400554:	31 db                	xor    %ebx,%ebx
  400556:	48 c1 fd 03          	sar    $0x3,%rbp
  40055a:	48 83 ec 08          	sub    $0x8,%rsp
  40055e:	e8 45 fe ff ff       	callq  4003a8 <_init>
  400563:	48 85 ed             	test   %rbp,%rbp
  400566:	74 1e                	je     400586 <__libc_csu_init+0x56>
  400568:	0f 1f 84 00 00 00 00 	nopl   0x0(%rax,%rax,1)
  40056f:	00 
  400570:	4c 89 ea             	mov    %r13,%rdx
  400573:	4c 89 f6             	mov    %r14,%rsi
  400576:	44 89 ff             	mov    %r15d,%edi
  400579:	41 ff 14 dc          	callq  *(%r12,%rbx,8)
  40057d:	48 83 c3 01          	add    $0x1,%rbx
  400581:	48 39 eb             	cmp    %rbp,%rbx
  400584:	75 ea                	jne    400570 <__libc_csu_init+0x40>
  400586:	48 83 c4 08          	add    $0x8,%rsp
  40058a:	5b                   	pop    %rbx
  40058b:	5d                   	pop    %rbp
  40058c:	41 5c                	pop    %r12
  40058e:	41 5d                	pop    %r13
  400590:	41 5e                	pop    %r14
  400592:	41 5f                	pop    %r15
  400594:	c3                   	retq   
  400595:	66 66 2e 0f 1f 84 00 	data32 nopw %cs:0x0(%rax,%rax,1)
  40059c:	00 00 00 00 

00000000004005a0 <__libc_csu_fini>:
  4005a0:	f3 c3                	repz retq 

Disassembly of section .fini:

00000000004005a4 <_fini>:
  4005a4:	48 83 ec 08          	sub    $0x8,%rsp
  4005a8:	48 83 c4 08          	add    $0x8,%rsp
  4005ac:	c3                   	retq   

Disassembly of section .rodata:

00000000004005b0 <_IO_stdin_used>:
  4005b0:	01 00                	add    %eax,(%rax)
  4005b2:	02 00                	add    (%rax),%al

Disassembly of section .eh_frame_hdr:

00000000004005b4 <.eh_frame_hdr>:
  4005b4:	01 1b                	add    %ebx,(%rbx)
  4005b6:	03 3b                	add    (%rbx),%edi
  4005b8:	38 00                	cmp    %al,(%rax)
  4005ba:	00 00                	add    %al,(%rax)
  4005bc:	06                   	(bad)  
  4005bd:	00 00                	add    %al,(%rax)
  4005bf:	00 1c fe             	add    %bl,(%rsi,%rdi,8)
  4005c2:	ff                   	(bad)  
  4005c3:	ff 84 00 00 00 4c fe 	incl   -0x1b40000(%rax,%rax,1)
  4005ca:	ff                   	(bad)  
  4005cb:	ff 54 00 00          	callq  *0x0(%rax,%rax,1)
  4005cf:	00 39                	add    %bh,(%rcx)
  4005d1:	ff                   	(bad)  
  4005d2:	ff                   	(bad)  
  4005d3:	ff ac 00 00 00 54 ff 	ljmpq  *-0xac0000(%rax,%rax,1)
  4005da:	ff                   	(bad)  
  4005db:	ff cc                	dec    %esp
  4005dd:	00 00                	add    %al,(%rax)
  4005df:	00 7c ff ff          	add    %bh,-0x1(%rdi,%rdi,8)
  4005e3:	ff                   	(bad)  
  4005e4:	ec                   	in     (%dx),%al
  4005e5:	00 00                	add    %al,(%rax)
  4005e7:	00 ec                	add    %ch,%ah
  4005e9:	ff                   	(bad)  
  4005ea:	ff                   	(bad)  
  4005eb:	ff 34 01             	pushq  (%rcx,%rax,1)
	...

Disassembly of section .eh_frame:

00000000004005f0 <__FRAME_END__-0x110>:
  4005f0:	14 00                	adc    $0x0,%al
  4005f2:	00 00                	add    %al,(%rax)
  4005f4:	00 00                	add    %al,(%rax)
  4005f6:	00 00                	add    %al,(%rax)
  4005f8:	01 7a 52             	add    %edi,0x52(%rdx)
  4005fb:	00 01                	add    %al,(%rcx)
  4005fd:	78 10                	js     40060f <_IO_stdin_used+0x5f>
  4005ff:	01 1b                	add    %ebx,(%rbx)
  400601:	0c 07                	or     $0x7,%al
  400603:	08 90 01 07 10 14    	or     %dl,0x14100701(%rax)
  400609:	00 00                	add    %al,(%rax)
  40060b:	00 1c 00             	add    %bl,(%rax,%rax,1)
  40060e:	00 00                	add    %al,(%rax)
  400610:	f0 fd                	lock std 
  400612:	ff                   	(bad)  
  400613:	ff 2a                	ljmpq  *(%rdx)
	...
  40061d:	00 00                	add    %al,(%rax)
  40061f:	00 14 00             	add    %dl,(%rax,%rax,1)
  400622:	00 00                	add    %al,(%rax)
  400624:	00 00                	add    %al,(%rax)
  400626:	00 00                	add    %al,(%rax)
  400628:	01 7a 52             	add    %edi,0x52(%rdx)
  40062b:	00 01                	add    %al,(%rcx)
  40062d:	78 10                	js     40063f <_IO_stdin_used+0x8f>
  40062f:	01 1b                	add    %ebx,(%rbx)
  400631:	0c 07                	or     $0x7,%al
  400633:	08 90 01 00 00 24    	or     %dl,0x24000001(%rax)
  400639:	00 00                	add    %al,(%rax)
  40063b:	00 1c 00             	add    %bl,(%rax,%rax,1)
  40063e:	00 00                	add    %al,(%rax)
  400640:	90                   	nop
  400641:	fd                   	std    
  400642:	ff                   	(bad)  
  400643:	ff 30                	pushq  (%rax)
  400645:	00 00                	add    %al,(%rax)
  400647:	00 00                	add    %al,(%rax)
  400649:	0e                   	(bad)  
  40064a:	10 46 0e             	adc    %al,0xe(%rsi)
  40064d:	18 4a 0f             	sbb    %cl,0xf(%rdx)
  400650:	0b 77 08             	or     0x8(%rdi),%esi
  400653:	80 00 3f             	addb   $0x3f,(%rax)
  400656:	1a 3b                	sbb    (%rbx),%bh
  400658:	2a 33                	sub    (%rbx),%dh
  40065a:	24 22                	and    $0x22,%al
  40065c:	00 00                	add    %al,(%rax)
  40065e:	00 00                	add    %al,(%rax)
  400660:	1c 00                	sbb    $0x0,%al
  400662:	00 00                	add    %al,(%rax)
  400664:	44 00 00             	add    %r8b,(%rax)
  400667:	00 85 fe ff ff 1b    	add    %al,0x1bfffffe(%rbp)
  40066d:	00 00                	add    %al,(%rax)
  40066f:	00 00                	add    %al,(%rax)
  400671:	41 0e                	rex.B (bad) 
  400673:	10 86 02 43 0d 06    	adc    %al,0x60d4302(%rsi)
  400679:	56                   	push   %rsi
  40067a:	0c 07                	or     $0x7,%al
  40067c:	08 00                	or     %al,(%rax)
  40067e:	00 00                	add    %al,(%rax)
  400680:	1c 00                	sbb    $0x0,%al
  400682:	00 00                	add    %al,(%rax)
  400684:	64 00 00             	add    %al,%fs:(%rax)
  400687:	00 80 fe ff ff 1b    	add    %al,0x1bfffffe(%rax)
  40068d:	00 00                	add    %al,(%rax)
  40068f:	00 00                	add    %al,(%rax)
  400691:	41 0e                	rex.B (bad) 
  400693:	10 86 02 43 0d 06    	adc    %al,0x60d4302(%rsi)
  400699:	56                   	push   %rsi
  40069a:	0c 07                	or     $0x7,%al
  40069c:	08 00                	or     %al,(%rax)
  40069e:	00 00                	add    %al,(%rax)
  4006a0:	44 00 00             	add    %r8b,(%rax)
  4006a3:	00 84 00 00 00 88 fe 	add    %al,-0x1780000(%rax,%rax,1)
  4006aa:	ff                   	(bad)  
  4006ab:	ff 65 00             	jmpq   *0x0(%rbp)
  4006ae:	00 00                	add    %al,(%rax)
  4006b0:	00 42 0e             	add    %al,0xe(%rdx)
  4006b3:	10 8f 02 45 0e 18    	adc    %cl,0x180e4502(%rdi)
  4006b9:	8e 03                	mov    (%rbx),%es
  4006bb:	45 0e                	rex.RB (bad) 
  4006bd:	20 8d 04 45 0e 28    	and    %cl,0x280e4504(%rbp)
  4006c3:	8c 05 48 0e 30 86    	mov    %es,-0x79cff1b8(%rip)        # ffffffff86701511 <_end+0xffffffff861004d1>
  4006c9:	06                   	(bad)  
  4006ca:	48 0e                	rex.W (bad) 
  4006cc:	38 83 07 4d 0e 40    	cmp    %al,0x400e4d07(%rbx)
  4006d2:	6c                   	insb   (%dx),%es:(%rdi)
  4006d3:	0e                   	(bad)  
  4006d4:	38 41 0e             	cmp    %al,0xe(%rcx)
  4006d7:	30 41 0e             	xor    %al,0xe(%rcx)
  4006da:	28 42 0e             	sub    %al,0xe(%rdx)
  4006dd:	20 42 0e             	and    %al,0xe(%rdx)
  4006e0:	18 42 0e             	sbb    %al,0xe(%rdx)
  4006e3:	10 42 0e             	adc    %al,0xe(%rdx)
  4006e6:	08 00                	or     %al,(%rax)
  4006e8:	14 00                	adc    $0x0,%al
  4006ea:	00 00                	add    %al,(%rax)
  4006ec:	cc                   	int3   
  4006ed:	00 00                	add    %al,(%rax)
  4006ef:	00 b0 fe ff ff 02    	add    %dh,0x2fffffe(%rax)
	...

0000000000400700 <__FRAME_END__>:
  400700:	00 00                	add    %al,(%rax)
	...

Disassembly of section .init_array:

0000000000600e10 <__frame_dummy_init_array_entry>:
  600e10:	c0 04 40 00          	rolb   $0x0,(%rax,%rax,2)
  600e14:	00 00                	add    %al,(%rax)
	...

Disassembly of section .fini_array:

0000000000600e18 <__do_global_dtors_aux_fini_array_entry>:
  600e18:	a0                   	.byte 0xa0
  600e19:	04 40                	add    $0x40,%al
  600e1b:	00 00                	add    %al,(%rax)
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
  600e40:	a8 03                	test   $0x3,%al
  600e42:	40 00 00             	add    %al,(%rax)
  600e45:	00 00                	add    %al,(%rax)
  600e47:	00 0d 00 00 00 00    	add    %cl,0x0(%rip)        # 600e4d <_DYNAMIC+0x25>
  600e4d:	00 00                	add    %al,(%rax)
  600e4f:	00 a4 05 40 00 00 00 	add    %ah,0x40(%rbp,%rax,1)
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
  600eaf:	00 00                	add    %al,(%rax)
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
  600ecf:	00 38                	add    %bh,(%rax)
  600ed1:	00 00                	add    %al,(%rax)
  600ed3:	00 00                	add    %al,(%rax)
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
  600f10:	30 00                	xor    %al,(%rax)
  600f12:	00 00                	add    %al,(%rax)
  600f14:	00 00                	add    %al,(%rax)
  600f16:	00 00                	add    %al,(%rax)
  600f18:	14 00                	adc    $0x0,%al
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
  600f2f:	00 78 03             	add    %bh,0x3(%rax)
  600f32:	40 00 00             	add    %al,(%rax)
  600f35:	00 00                	add    %al,(%rax)
  600f37:	00 07                	add    %al,(%rdi)
  600f39:	00 00                	add    %al,(%rax)
  600f3b:	00 00                	add    %al,(%rax)
  600f3d:	00 00                	add    %al,(%rax)
  600f3f:	00 60 03             	add    %ah,0x3(%rax)
  600f42:	40 00 00             	add    %al,(%rax)
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
  600f6f:	00 40 03             	add    %al,0x3(%rax)
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
  600f8f:	00 38                	add    %bh,(%rax)
  600f91:	03 40 00             	add    0x0(%rax),%eax
	...

Disassembly of section .got:

0000000000600ff8 <.got>:
	...

Disassembly of section .got.plt:

0000000000601000 <_GLOBAL_OFFSET_TABLE_>:
  601000:	28 0e                	sub    %cl,(%rsi)
  601002:	60                   	(bad)  
	...
  601017:	00 e6                	add    %ah,%dh
  601019:	03 40 00             	add    0x0(%rax),%eax
  60101c:	00 00                	add    %al,(%rax)
  60101e:	00 00                	add    %al,(%rax)
  601020:	f6 03 40             	testb  $0x40,(%rbx)
  601023:	00 00                	add    %al,(%rax)
  601025:	00 00                	add    %al,(%rax)
	...

Disassembly of section .data:

0000000000601028 <__data_start>:
	...

0000000000601030 <__dso_handle>:
	...

Disassembly of section .bss:

0000000000601038 <__bss_start>:
	...

Disassembly of section .comment:

0000000000000000 <.comment>:
   0:	47                   	rex.RXB
   1:	43                   	rex.XB
   2:	43 3a 20             	rex.XB cmp (%r8),%spl
   5:	28 55 62             	sub    %dl,0x62(%rbp)
   8:	75 6e                	jne    78 <_init-0x400330>
   a:	74 75                	je     81 <_init-0x400327>
   c:	20 34 2e             	and    %dh,(%rsi,%rbp,1)
   f:	38 2e                	cmp    %ch,(%rsi)
  11:	34 2d                	xor    $0x2d,%al
  13:	32 75 62             	xor    0x62(%rbp),%dh
  16:	75 6e                	jne    86 <_init-0x400322>
  18:	74 75                	je     8f <_init-0x400319>
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
  31:	75 6e                	jne    a1 <_init-0x400307>
  33:	74 75                	je     aa <_init-0x4002fe>
  35:	20 34 2e             	and    %dh,(%rsi,%rbp,1)
  38:	38 2e                	cmp    %ch,(%rsi)
  3a:	32 2d 31 39 75 62    	xor    0x62753931(%rip),%ch        # 62753971 <_end+0x62152931>
  40:	75 6e                	jne    b0 <_init-0x4002f8>
  42:	74 75                	je     b9 <_init-0x4002ef>
  44:	31 29                	xor    %ebp,(%rcx)
  46:	20 34 2e             	and    %dh,(%rsi,%rbp,1)
  49:	38 2e                	cmp    %ch,(%rsi)
  4b:	32 00                	xor    (%rax),%al
```

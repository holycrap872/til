	.file	"simple.cpp"
	.section	.text.startup,"ax",@progbits
	.align	16, 0x90
	.type	__cxx_global_var_init,@function
__cxx_global_var_init:                  # @__cxx_global_var_init
	.cfi_startproc
# BB#0:
	pushq	%rbp
.Ltmp2:
	.cfi_def_cfa_offset 16
.Ltmp3:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
.Ltmp4:
	.cfi_def_cfa_register %rbp
	subq	$16, %rsp
	leaq	_ZStL8__ioinit, %rdi
	callq	_ZNSt8ios_base4InitC1Ev
	leaq	_ZNSt8ios_base4InitD1Ev, %rdi
	leaq	_ZStL8__ioinit, %rsi
	leaq	__dso_handle, %rdx
	callq	__cxa_atexit
	movl	%eax, -4(%rbp)          # 4-byte Spill
	addq	$16, %rsp
	popq	%rbp
	ret
.Ltmp5:
	.size	__cxx_global_var_init, .Ltmp5-__cxx_global_var_init
	.cfi_endproc

	.text
	.globl	main
	.align	16, 0x90
	.type	main,@function
main:                                   # @main
	.cfi_startproc
# BB#0:
	pushq	%rbp
.Ltmp8:
	.cfi_def_cfa_offset 16
.Ltmp9:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
.Ltmp10:
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	movl	$0, -4(%rbp)
	movl	%edi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	cmpl	$2, -8(%rbp)
	jle	.LBB1_2
# BB#1:
	leaq	_ZSt4cout, %rdi
	leaq	.L.str, %rsi
	callq	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%rax, -24(%rbp)         # 8-byte Spill
	jmp	.LBB1_3
.LBB1_2:
	leaq	_ZSt4cout, %rdi
	leaq	.L.str1, %rsi
	callq	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
	movq	%rax, -32(%rbp)         # 8-byte Spill
.LBB1_3:
	movl	-4(%rbp), %eax
	addq	$32, %rsp
	popq	%rbp
	ret
.Ltmp11:
	.size	main, .Ltmp11-main
	.cfi_endproc

	.section	.text.startup,"ax",@progbits
	.align	16, 0x90
	.type	_GLOBAL__I_a,@function
_GLOBAL__I_a:                           # @_GLOBAL__I_a
	.cfi_startproc
# BB#0:
	pushq	%rbp
.Ltmp14:
	.cfi_def_cfa_offset 16
.Ltmp15:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
.Ltmp16:
	.cfi_def_cfa_register %rbp
	callq	__cxx_global_var_init
	popq	%rbp
	ret
.Ltmp17:
	.size	_GLOBAL__I_a, .Ltmp17-_GLOBAL__I_a
	.cfi_endproc

	.type	_ZStL8__ioinit,@object  # @_ZStL8__ioinit
	.local	_ZStL8__ioinit
	.comm	_ZStL8__ioinit,1,1
	.type	.L.str,@object          # @.str
	.section	.rodata.str1.1,"aMS",@progbits,1
.L.str:
	.asciz	"hi\n"
	.size	.L.str, 4

	.type	.L.str1,@object         # @.str1
.L.str1:
	.asciz	"bye\n"
	.size	.L.str1, 5

	.section	.init_array,"aw",@init_array
	.align	8
	.quad	_GLOBAL__I_a

	.ident	"Ubuntu clang version 3.4-1ubuntu3 (tags/RELEASE_34/final) (based on LLVM 3.4)"
	.section	".note.GNU-stack","",@progbits

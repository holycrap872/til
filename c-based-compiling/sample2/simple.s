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
	.cfi_personality 3, __gxx_personality_v0
.Leh_func_begin1:
	.cfi_lsda 3, .Lexception1
# BB#0:
	pushq	%rbp
.Ltmp20:
	.cfi_def_cfa_offset 16
.Ltmp21:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
.Ltmp22:
	.cfi_def_cfa_register %rbp
	subq	$80, %rsp
	movl	$0, -4(%rbp)
	movl	%edi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movl	-8(%rbp), %esi
	leaq	-24(%rbp), %rax
	movq	%rax, %rdi
	movq	%rax, -48(%rbp)         # 8-byte Spill
	callq	_ZN6PersonC1Ej
.Ltmp6:
	movq	-48(%rbp), %rdi         # 8-byte Reload
	callq	_ZN6Person11anotherYearEv
.Ltmp7:
	jmp	.LBB1_1
.LBB1_1:
.Ltmp8:
	leaq	-24(%rbp), %rdi
	callq	_ZN6Person6getAgeEv
.Ltmp9:
	movl	%eax, -52(%rbp)         # 4-byte Spill
	jmp	.LBB1_2
.LBB1_2:
	movl	-52(%rbp), %eax         # 4-byte Reload
	cmpl	$2, %eax
	jbe	.LBB1_6
# BB#3:
.Ltmp12:
	movl	$_ZSt4cout, %eax
	movl	%eax, %edi
	movl	$.L.str, %eax
	movl	%eax, %esi
	callq	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
.Ltmp13:
	movq	%rax, -64(%rbp)         # 8-byte Spill
	jmp	.LBB1_4
.LBB1_4:
	jmp	.LBB1_8
.LBB1_5:
.Ltmp14:
	movl	%edx, %ecx
	movq	%rax, -32(%rbp)
	movl	%ecx, -36(%rbp)
.Ltmp15:
	leaq	-24(%rbp), %rdi
	callq	_ZN6PersonD1Ev
.Ltmp16:
	jmp	.LBB1_9
.LBB1_6:
.Ltmp10:
	movl	$_ZSt4cout, %eax
	movl	%eax, %edi
	movl	$.L.str1, %eax
	movl	%eax, %esi
	callq	_ZStlsISt11char_traitsIcEERSt13basic_ostreamIcT_ES5_PKc
.Ltmp11:
	movq	%rax, -72(%rbp)         # 8-byte Spill
	jmp	.LBB1_7
.LBB1_7:
	jmp	.LBB1_8
.LBB1_8:
	leaq	-24(%rbp), %rdi
	callq	_ZN6PersonD1Ev
	movl	-4(%rbp), %eax
	addq	$80, %rsp
	popq	%rbp
	ret
.LBB1_9:
	jmp	.LBB1_10
.LBB1_10:
	movq	-32(%rbp), %rdi
	callq	_Unwind_Resume
.LBB1_11:
.Ltmp17:
	movl	%edx, %ecx
	movq	%rax, %rdi
	movl	%ecx, -76(%rbp)         # 4-byte Spill
	callq	__clang_call_terminate
.Ltmp23:
	.size	main, .Ltmp23-main
	.cfi_endproc
.Leh_func_end1:
	.section	.gcc_except_table,"a",@progbits
	.align	4
GCC_except_table1:
.Lexception1:
	.byte	255                     # @LPStart Encoding = omit
	.byte	3                       # @TType Encoding = udata4
	.byte	73                      # @TType base offset
	.byte	3                       # Call site Encoding = udata4
	.byte	65                      # Call site table length
.Lset0 = .Leh_func_begin1-.Leh_func_begin1 # >> Call Site 1 <<
	.long	.Lset0
.Lset1 = .Ltmp6-.Leh_func_begin1        #   Call between .Leh_func_begin1 and .Ltmp6
	.long	.Lset1
	.long	0                       #     has no landing pad
	.byte	0                       #   On action: cleanup
.Lset2 = .Ltmp6-.Leh_func_begin1        # >> Call Site 2 <<
	.long	.Lset2
.Lset3 = .Ltmp13-.Ltmp6                 #   Call between .Ltmp6 and .Ltmp13
	.long	.Lset3
.Lset4 = .Ltmp14-.Leh_func_begin1       #     jumps to .Ltmp14
	.long	.Lset4
	.byte	0                       #   On action: cleanup
.Lset5 = .Ltmp15-.Leh_func_begin1       # >> Call Site 3 <<
	.long	.Lset5
.Lset6 = .Ltmp16-.Ltmp15                #   Call between .Ltmp15 and .Ltmp16
	.long	.Lset6
.Lset7 = .Ltmp17-.Leh_func_begin1       #     jumps to .Ltmp17
	.long	.Lset7
	.byte	1                       #   On action: 1
.Lset8 = .Ltmp10-.Leh_func_begin1       # >> Call Site 4 <<
	.long	.Lset8
.Lset9 = .Ltmp11-.Ltmp10                #   Call between .Ltmp10 and .Ltmp11
	.long	.Lset9
.Lset10 = .Ltmp14-.Leh_func_begin1      #     jumps to .Ltmp14
	.long	.Lset10
	.byte	0                       #   On action: cleanup
.Lset11 = .Ltmp11-.Leh_func_begin1      # >> Call Site 5 <<
	.long	.Lset11
.Lset12 = .Leh_func_end1-.Ltmp11        #   Call between .Ltmp11 and .Leh_func_end1
	.long	.Lset12
	.long	0                       #     has no landing pad
	.byte	0                       #   On action: cleanup
	.byte	1                       # >> Action Record 1 <<
                                        #   Catch TypeInfo 1
	.byte	0                       #   No further actions
                                        # >> Catch TypeInfos <<
	.long	0                       # TypeInfo 1
	.align	4

	.section	.text._ZN6Person6getAgeEv,"axG",@progbits,_ZN6Person6getAgeEv,comdat
	.weak	_ZN6Person6getAgeEv
	.align	16, 0x90
	.type	_ZN6Person6getAgeEv,@function
_ZN6Person6getAgeEv:                    # @_ZN6Person6getAgeEv
	.cfi_startproc
# BB#0:
	pushq	%rbp
.Ltmp26:
	.cfi_def_cfa_offset 16
.Ltmp27:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
.Ltmp28:
	.cfi_def_cfa_register %rbp
	movq	%rdi, -8(%rbp)
	movq	-8(%rbp), %rdi
	movl	(%rdi), %eax
	popq	%rbp
	ret
.Ltmp29:
	.size	_ZN6Person6getAgeEv, .Ltmp29-_ZN6Person6getAgeEv
	.cfi_endproc

	.section	.text.__clang_call_terminate,"axG",@progbits,__clang_call_terminate,comdat
	.hidden	__clang_call_terminate
	.weak	__clang_call_terminate
	.align	16, 0x90
	.type	__clang_call_terminate,@function
__clang_call_terminate:                 # @__clang_call_terminate
# BB#0:
	pushq	%rbp
	movq	%rsp, %rbp
	subq	$16, %rsp
	callq	__cxa_begin_catch
	movq	%rax, -8(%rbp)          # 8-byte Spill
	callq	_ZSt9terminatev
.Ltmp30:
	.size	__clang_call_terminate, .Ltmp30-__clang_call_terminate

	.section	.text.startup,"ax",@progbits
	.align	16, 0x90
	.type	_GLOBAL__I_a,@function
_GLOBAL__I_a:                           # @_GLOBAL__I_a
	.cfi_startproc
# BB#0:
	pushq	%rbp
.Ltmp33:
	.cfi_def_cfa_offset 16
.Ltmp34:
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
.Ltmp35:
	.cfi_def_cfa_register %rbp
	callq	__cxx_global_var_init
	popq	%rbp
	ret
.Ltmp36:
	.size	_GLOBAL__I_a, .Ltmp36-_GLOBAL__I_a
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

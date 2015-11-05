# Compile C-Language Code

I have compiled a lot of programs, but I always rush through.  Any problems
I encounter I google and pretty much just paste in, hoping they work.  What
follows is my attempt to understand what's going on a little better.

For my examples, I'll be using the simple c program located
[here](c-based-compiling/samples/simple.cpp)

## The Stages

Most C-based compilers are capable at stopping at various stages in the
compilation process.  For clang (which I'll be using) the stages are

1) Preprocessing : Macro expansion, #include expansion, and other preprocessor
   directives.  To generate this stage I ran `clang++ -E simple.cpp`.  This
   produces a ton of code directly to stdin.  When I redirected it into a file,
   the overall size was 451057 bytes.  It can be seen
   [here](c-based-compiling/samples/simple.e).  As can be noticed, this pulls
   in everything (including iostream and all of it's dependencies).  In
   addition, it's all in plain-text.  Future stages of compilation will
   dramatically shrink the output: this is due to linking to pre-compiled
   libraries and because it's in machine code, which is much more efficient
   with space.

   This is also the stage where missing includes and definition problems will
   be flagged.  If the goal is to expand the entire program, then clearly you
   need to be able to find everything

2) Parser and Type-checking : The name says it all.  Based on my understanding,
   the output from the pre-processor is fed into this stage, where it is turned
   into a series of ASTs so the program can be checked.  If compiled correctly
   nothing really happens after running...it just returns.  If there is an
   error, the program will identify it.  This is the stage that catches a lot
   of your stupid programming mistakes.  The other, harder to find ones come
   during linking and stuff.  The command to run this stage is
   `clang++ -fsyntax-only simple.cpp`

3) LLVM Generation : This stage is obviously specific to LLVM.  Here, the
   program is turned into an intermediate representation (IR) so that
   that optimizations can be performed on it.  From a larger standpoint, this
   architecture allows any programming language that can be distilled down to
   LLVM to benefit from the optimization passes that have been created.  A
   good way to think of it as many different languages funnel into the LLVM
   generation stage, where they are all handled in the same way.  After these
   optimizations are complete, the LLVM can be output to many different
   architectures.  To generate the LLVM code, simply run
   `clang++ -S simple.cpp`. The output can be seen
   [here](c-based-compiling/samples/simple.s).

   An interesting side note, adding the `static` flag at this stage does
   not increase the size of the output at all.  This shows two things...
   First, it seems to show that optimizations are not calculated across files.
   Second, it shows that it is assumed that the .o files necessary for creating
   a static file will be present at during linking, at which point everything
   will be bundled together.

4) Assembly Generation : This is the stage that translates LLVM to assembly
   code.  In this case, the translation is to an ELF object file.  The command
   to run this stage is `clang++ -c simple.cpp `The output is not super
   interesting but can be seen [here](c-based-compiling/samples/simple.o).

   It is again an interesting side not that adding the `static` flag does not
   increase the size of the output at all.

5) Linking : This stage takes various .o files that have been compiled elsewhere
   and turns it into a single executable.  The command to generate the
   executable is `clang -o simple simple.cpp`.  You can also take the generated
   `.o` file from the previous stage and link it via
   `clang++ -o simple simple.o`.

   Finally, as noted in the discussion in stage 3, adding the `static` flag at
   this point balloons the executable size from 9050 to 1625497 bytes.

## Header files

Each stage of described above relies on the one before it.  Another way to say
it is that each stage passes the information it calculates on to the next stage.
I haven't yet discovered how to capture the information from stage 1 and then
manually pass it into stage 2 or how to capture the output from stage 2 and
pass it into stage 3.  Stage 3, however, produces a `.s` file that can be
directly passed into stage 4 via the command `clang++ -c simple.s`, producing a
`.o` file. The same goes for `.o` files to executables.

This got me wondering...at what point do headers become superfluous and what
does that show about them?  Removing the header at stage 1 caused errors.
Namely "simple.cpp:1:10: fatal error: 'simple.hpp' file not found".
Interestingly, the Preprocessor created almost all of the fully expanded file
before finding the error on line 2.  This makes it seem likely that things
are processed in a depth first manner.

When using the `.s` file to create the `.o` file and when using the `.o` file
to create the executable, the header is not required.  This is illustrative of
the way c and cpp treat their headers.

## So What's Next

Now that I understand the basics, I'm going to break out the different things
I learn into sub 

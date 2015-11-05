# TIL

> Today I Learned

A collection of concise write-ups on small things I learn day to day across a
variety of languages and technologies. These are mostly things I learn by
working with smart people at [GrammaTech](http://grammatech.com).


### ELF

A lot of what my current job encompasses is binary analysis.  While
I had a general understanding of binary programs via various hardware
and machine organization courses, these document my attempts to take
that knowledge to real programs.

- [An "interactive" ELF experience](elf/elf_basics/README.md)

### Compiling C-Type Code

If I were to pick one thing I'm bad at, it would be this.  I've never
had the patience to try and actually figure out what's going on through
the different phases of compiling and linking.  NO MORE!!!

- [An "interactive" C experience](c-based-compiling/README.md)

### SCONS

SCONS is a build system that attempts to make all dependencies within
a particular system explicit.  By doing so, in theory, things like
enviroment variables will no longer make/break a build.  This enables
greater portability from machine to machine.

- [A preliminary review of the scons system](scons/scons.md)

### git-svn

A series of reminders/experiments when using git and git-svn

- [Checkout SVN Repo Using git-svn](git-svn/checkout-svn-repo.md)
- [Sparse checkouts of git repos](git-svn/sparse-checkouts.md))

### GDB

Things I wish someone had told me 3-4 years ago about GDB.  There's
a lot of good things about grad school, but on bad thing is that you
have no idea stuff like this exists.  More than anything I've learned
that if you want it, it probably exists.  You just have to find it.

- [Skipping Useless Files While Debugging](gdb/skipping-useless-files.md)
- [View Source Code While Debugging](gdb/source-code-view.md)
- [Flip through Different Views](gdb/gdb-panes.md)
- [Working with Binary Code](gdb/binary-code.md)

### VirtualBox

I use VMs everywhere, and even from time to time enter VM inception.
These are some small tips I picked up when working with VirtualBox
VMs that make them easier to use.

- [Set up Shared Folder](virtualbox/set-up-shared-folder.md)

## About

I shamelessly stole this idea from
[jbranchaud/til](https://github.com/jbranchaud/til) who in turn shamelessly
stole it from [thoughtbot/til](https://github.com/thoughtbot/til).

## Other TIL Collections

- [Today I Learned by Hashrocket](https://til.hashrocket.com)
- [jwworth/til](https://github.com/jwworth/til)
- [thoughtbot/til](https://github.com/thoughtbot/til)
- [jbranchaud/til](https://github.com/jbranchaud/til)

## License

&copy; 2015 Eric Rizzi

This repository is licensed under the MIT license. See `LICENSE` for
details.


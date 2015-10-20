# Scons

Scons is a python based build system that caches all of your configuration
information from build to build and determines which dependencies need to
be rebuilt.  At the most basic level, it's very similar to the make utility. 
On top of this base functionality, however, it has the ability to fetch
from remote repos, gathers dependencies from a developers build so that it
is easier to share across platforms, and calls the correct builder for a
large variety of program types, such as C, Java, Fortran, Latex...

## Passing in Arguments
Many of the build scripts that we use here say something like

```
exec python third-party/scons/scons.py $GTR_BUILD_ARGS "$@"
```

As an example of how to pass arguments in, assume we want to let
the build know that we are using git rather than svn (I encountered
this problem and it took me a while to figure out what was being
checked and where).

```
export GTR_BUILD_ARGS"git=true offsite=true"
./build
```

another option is simply

```
./build git=true offsite=true
```

To explain this problem a little further, scons was failing without
a whole lot of information as to why.  The only output it gave was
`svn info failed`.  Therefore, I grepped for svn in the scons folder
and found a likely line.  From there I traced the python scons file
to see that it was looking for a variable as to whether I used git
or svn.  I then passed in the information via the variable and it
proceeded to build.

Similarly, the stupid thing was failing without any warnings at all
other than saying it couldn't find some manual.  Therefore, after
~30 minutes of digging (thanks cons) I was finally able to figure out
why.  You have to set the offsite flag to true...not sure why.

It seems a particularly bad design decision to have a build script
that big fail silently.  I don't know who did that, but I'm not
real happy with them right now.

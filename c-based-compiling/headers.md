# Header files

Each compilation stage described in the [README](c-based-compiling/README.md)
relies on the calculations of the one preceding it.  Another way to say this
is that each stage passes the information it calculates on to the next stage.
I haven't yet discovered how to capture the information from stage 1 and then
manually pass it into stage 2 or how to capture the output from stage 2 and
pass it into stage 3.  Stage 3, however, produces a `.s` file that can be
directly passed into stage 4 via the command `clang++ -c simple.s`, producing a
`.o` file. The same goes for `.o` files to executables.

This got me wondering...at what point do headers become superfluous and what
does that show about them?  Removing `simple.hpp` and running the command
`clang++ -E simple.cpp` from within the `sample1` folder caused errors.
Namely "simple.cpp:1:10: fatal error: 'simple.hpp' file not found".
Interestingly, the Preprocessor created almost all of the fully expanded file
before finding the error on line 2.  This makes it seem likely that things
are processed in a depth first manner.

When using the `.s` file to create the `.o` file and when using the `.o` file
to create the executable, the header is not required. In order to create a
more illustrative case, I created a more complicated program (seen in the
folder "sample2").  The output of running `clang++ -E simple.cpp` can be seen
[here](c-based-compiling/sample2/simple.e).  Of particular note is the section
at the very bottom, repoduced here

```
class Person{
    private:
        unsigned int age;
        unsigned int eyes;
        static unsigned int population;

    public:
        Person(unsigned int);
        ~Person();
        void anotherYear();
        void accident(unsigned int eyesDamaged);

        unsigned int getAge(){
            return this->age;
        }

        unsigned int getEyes(){
            return this->eyes;
        }
};
# 4 "simple.cpp" 2

using namespace std;

int main(int argc, char * argv[]){
    Person p(argc);
    p.anotherYear();

    if (p.getAge() > 2) {
        cout << "hi\n";
    } else {
        cout << "bye\n";
    }
}
```

As can be seen, the macros in the original program have been replaced with
actual values.  What is most interesting, however, is that the
"simpleClass.hpp" file is included in it's entirety but *NOT* the actual
implementations of the all of the fuctions.  Of particular note is the
presence of the private variables.  Headers are intended to hide the specifics
of a class.  As has been
[pointed out](http://yosefk.com/c++fqa/picture.html#fqa-6.3), however, they
don't do that perfectly since private variables are included in headers.
Therefore, everytime the private variables are changed, not only must that
c/cpp file be recompiled, but everything that relies on it also must be
recompiled.

## Missing Headers

A missing include is fairly annoying.  Up will pop something like
"simple.cpp:2:10: fatal error: 'simple.hpp' file not found".  There are
two basic types of headers

1) System Headers : These are represented by `<XXX>`

2) Local Headers : These are represented by `"XXX"`

System headers are found in places like `/usr/include/c++/4.7`.  The compiler
will look in all of the normal places when looking for these.  Local headers
are looked for in the folder of the ".cpp" that is being compiled.  You can
easily exand the search by adding `-I/location/of/header`.  This will add
the path to both the Local and System header lookups.

To illustrate this point, I `cd sample2 && mv simple.hpp .. && clang++ -E -I.. simple.cpp`.
Everything compiled beautifully.  To examine what was actually happening, I
reran the command with the `-v` flag, generating the output

```
Selected GCC installation: /usr/bin/../lib/gcc/x86_64-linux-gnu/4.8

 "/usr/bin/clang" -cc1 -triple x86_64-pc-linux-gnu -E -disable-free
-disable-llvm-verifier -main-file-name simple.cpp -mrelocation-model static
-mdisable-fp-elim -fmath-errno -masm-verbose -mconstructor-aliases
-munwind-tables -fuse-init-array -target-cpu x86-64 -target-linker-version 2.24
-v -resource-dir /usr/bin/../lib/clang/3.4 -I .. -internal-isystem
/usr/bin/../lib/gcc/x86_64-linux-gnu/4.8/../../../../include/c++/4.8
-internal-isystem /usr/bin/../lib/gcc/x86_64-linux-gnu/4.8/../../../
../include/c++/4.8/x86_64-linux-gnu -internal-isystem /usr/bin/../lib
/gcc/x86_64-linux-gnu/4.8/../../../../include/c++/4.8/backward
-internal-isystem /usr/bin/../lib/gcc/x86_64-linux-gnu/4.8/../../../
../include/x86_64-linux-gnu/c++/4.8 -internal-isystem /usr/local/include
-internal-isystem /usr/bin/../lib/clang/3.4/include -internal-externc-isystem
/usr/bin/../lib/gcc/x86_64-linux-gnu/4.8/include -internal-externc-isystem
/usr/include/x86_64-linux-gnu -internal-externc-isystem /include
-internal-externc-isystem /usr/include -fdeprecated-macro -fdebug-compilation-dir
/home/ziggy/Documents/workspace/til/c-based-compiling/sample2 -ferror-limit 19
-fmessage-length 80 -mstackrealign -fobjc-runtime=gcc -fcxx-exceptions
fexceptions -fdiagnostics-show-option -fcolor-diagnostics -vectorize-slp -o -
-x c++ simple.cpp

clang -cc1 version 3.4 based upon LLVM 3.4 default target x86_64-pc-linux-gnu

ignoring nonexistent directory "/usr/bin/../lib/gcc/x86_64-linux-gnu/4.8/../
../../../include/c++/4.8/x86_64-linux-gnu"

ignoring nonexistent directory "/include"

#include "..." search starts here:
#include <...> search starts here:
 ..
```
This is the -I we set
```
 /usr/bin/../lib/gcc/x86_64-linux-gnu/4.8/../../../../include/c++/4.8
 /usr/bin/../lib/gcc/x86_64-linux-gnu/4.8/../../../../include/c++/4.8/backward
 /usr/bin/../lib/gcc/x86_64-linux-gnu/4.8/../../../../include/x86_64-linux-gnu/c++/4.8
 /usr/local/include
 /usr/bin/../lib/clang/3.4/include
 /usr/bin/../lib/gcc/x86_64-linux-gnu/4.8/include
 /usr/include/x86_64-linux-gnu
 /usr/include
End of search list.
```

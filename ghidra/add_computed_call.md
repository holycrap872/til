## Adding Computed Call to Ghidra

Ghidra does it's best to compute the call graph of any program that it is given.
Some call-graph patterns are really easy to handle.  For example, the functions

```
void f1() {
  printf("hi\n");
}

void f2() {
  f1();
}

void f3() {
  f1();
}

void f4() {
  f2();
  f3();
}
```

Would create the call-graph:

```
   f4
  /  \
 f2  f3
  \  /
   f1
```

Unfortunately, some call-graph patterns are much more difficult to directly
compute.  For example, indirect/computed calls.  In assembly they look something
like:

```
call $rax
```

In this case, you may need to "discover" where these call(s) go to and augment
Ghidra's call graph.  This can be done with the following steps.

1) Go to the listing and find the instruction that is doing the indirect/computed
   call.
    - ex: `blx $r12` for ARM

2) Right click on the instruction

3) Select `References->Add Reference From`
    - I would have called it `Add Reference To/From`, but I'm sure there's a
      technical reason why they didn't.

4) Select the `memory` radio box and put in the address/type of the call.

5) You (may) need to restart Ghidra to have this new information "soak" into
   the call graph.

6) Now, when selecting the `Function Call Graph` of the target function, you
   should see the function containing the indirect/computed jump as a parent.

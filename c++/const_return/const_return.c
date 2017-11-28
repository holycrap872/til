#include <stdio.h>
#include <stdlib.h>

const int *
get_num1()
{
    int* x = (int*) malloc(sizeof(int) * 1);
    *x = 1;
    return x;
}


int * const
get_num2()
{
    int * x = (int*) malloc(sizeof(int) * 1);
    *x = 2;
    return x;
}


const int * const
get_num3()
{
    int * x = (int*) malloc(sizeof(int) * 1);
    *x = 3;
    return x;
}


const int
get_num4()
{
    return 4;
}


int
main()
{
    // The `const` is necesssary since the integer pointed to is unchanging.
    const int* x1 = get_num1();
    x1 = get_num1();
    // (*x1)++;


    // The`const` can be dropped due to copy by value in the return
    int* x2_1 = get_num2();
    x2_1 = get_num2();
    (*x2_1)++;


    // When including the `const` however, now the pointer in the scope cannot
    // be changed (although it's value can).
    int* const x2_2 = get_num2();
    (*x2_2)++;
    // x2_2 = get_num2();


    // The `const` is necesssary since the integer pointed to is unchanging.
    // The second const can be dropped do to copy by value in the return
    const int* x3 = get_num3();
    // (*x3)++;
    x3 = get_num3();


    // The const can be dropped due to return by value.  At one point, important
    // people suggested making all user-defined types const when returned from
    // a function (to prevent things like `(x + y) = z;`).  This suggestion,
    // however, has become obselete due to C++11's ability to "take full
    // advantage of rvalue references" (i.e. to reduce the need to return by
    // value).
    int x4 = get_num4();

    return *x1 + *x2_1 + *x2_2 + *x3 + x4;
}


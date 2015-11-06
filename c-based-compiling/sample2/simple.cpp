#include <iostream>
#include "simple.hpp"
#include "simpleClass.hpp"

using namespace std;

int main(int argc, char * argv[]){
    Person p(argc);
    p.anotherYear();

    if (p.getAge() > VALUE) {
        cout << HI;
    } else {
        cout << BYE;
    }
}

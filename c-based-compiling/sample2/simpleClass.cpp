#include <iostream>
#include "simpleClass.hpp"

//namespace eric{

unsigned int Person::population = 0;

Person::Person(unsigned int age){
    this->age = age;
    Person::population ++;
}

Person::~Person(){
    Person::population --;
}

void Person::anotherYear() {
    std::cout << "autumn turns to fall\n";
    age ++;
}

void Person::accident(unsigned int eyesDamaged){
    if(eyesDamaged >= eyes){
        eyes = 0;
    }else{
        eyes -= eyesDamaged;
    }
}

//}


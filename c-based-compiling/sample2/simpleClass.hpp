#ifndef PERSON_HPP
#define PERSON_HPP
//namespace eric{

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

//}
#endif

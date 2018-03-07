#include <stdio.h>
#include <string>

class Person{

public:
    Person(const std::string name, unsigned age)
    : m_name(name)
    , m_age(age)
    { }

    Person(const Person & other)
    : m_name(other.m_name)
    , m_age(other.m_age + 1)
    { }

    // This seems to cause undefined behaviour.  The general consensus seems
    // to be that you can either have the assignment operator, or you can have
    // const members, but not both.
    //Person & operator=(const Person & rhs) {
    //    return *(new Person(rhs.m_name, rhs.m_age));
    //}

    ~Person() {}

    std::string get_name() const { return m_name; }
    unsigned get_age() const { return m_age; }

private:
    const std::string m_name;
    const unsigned m_age;
};

int
main()
{
    Person p("Eric", 30);
    Person q(p);

    // And yet somehow the compiler figures it out.
    Person e = q;

    printf("%s is %d years old\n", e.get_name().c_str(), e.get_age());
}

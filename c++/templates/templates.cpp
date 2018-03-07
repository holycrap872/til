#include <string>
#include <stdio.h>

class One {

public:
  One(std::string name)
  : m_name(name)
  {}

  ~One() {}

  std::string get_name() const { return m_name; }

private:
  std::string m_name;

};

class Two {

public:
  Two() {}
  ~Two() {}

  std::string get_name() const { return "Two"; }

};


template <typename T>
void
print_name(const T & t) {
    printf("%s\n", t.get_name().c_str());
}


int
main() {
    One one("One");
    Two two;

    print_name(one);
    print_name(two);

    return 0;
}

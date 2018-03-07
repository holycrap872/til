#include <string>
#include <stdio.h>

template <size_t WD1, size_t WD2>
class Button{

public:
  Button()
  : m_count(0)
  {}

  ~Button() {}

  void add1() { m_count += WD1; }
  void add2() { m_count += WD2; }
  void print() { printf("%d\n", m_count); }

private:
  int m_count;

};


int
main()
{
    Button<5, 7> b1;
    b1.add1();
    b1.add2();
    b1.print();

    Button<10, 17> b2;
    b2.add1();
    b2.add2();
    b2.print();
}

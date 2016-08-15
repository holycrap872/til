# Python quick hits

## Named tuples

```
from collections import namedtuple


Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")
perry.age = 42
```

[thanks](https://pythontips.com/2015/06/06/why-should-you-use-namedtuple-instead-of-a-tuple/#more-620)

## Deque

```
from collections import deque

d = deque()
d += [1] # equivant to d.append
d.appendleft(0)
assert d == [0, 1]

d.extend([2,3])
d.extendleft([-2,-1])
assert d == [-2, -1, 0, 1, 2, 3]

assert d.rotate() `is equivalent` d.appendleft(d.pop())
```

# Iterables

```
>>> open('test.py')
<_io.TextIOWrapper name='test.py' mode='r' encoding='UTF-8'>
>>> f = open('test.py')
>>> f.readline()
'import time\n'
>>> f.readline()
'print("Time is here")\n'
>>> f.readline()
'username = "utkarshsingh"\n'
>>> f.readline()
'print(f"Hello {username}")'
>>> f.readline()
''
```

### \_\_next\_\_
```
>>> f = open('test.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("Time is here")\n'
>>> f.__next__()
'username = "utkarshsingh"\n'
>>> f.__next__()
'print(f"Hello {username}")'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration           #exception raised
```

### Using for loop
```
>>> for line in open('test.py'):
...     print(line)
... 
import time

print("Time is here")

username = "utkarshsingh"

print(f"Hello {username}")
>>> 
```

### while loop
```
>>> f = open('test.py')
>>> while True:
...     line = f.readline()
...     if not line: break
...     print(line, end='')
... 
import time
print("Time is here")
username = "utkarshsingh"
print(f"Hello {username}")
```

## Iteration tools

```
>>> myList = [1,2,3,4]
>>> I = iter(myList)
>>> I
<list_iterator object at 0x7f5b3a55dc00>
>>> I.__next__()
1
>>> I
<list_iterator object at 0x7f5b3a55dc00>
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

### In case of a file the iterating pointers are handled by default
```
>>> f = open('test.py')
>>> iter(f) is f
True

>>> iter(f) is f.__iter__()
True
```

In case of a list:
```
>>> myList
[1, 2, 3, 4, 5, 6]
>>> iter(myList) is myList.__iter__()
False
```

Dictionary:
```
>>> D = {'a' : 1, 'b' : 2}
>>> for key in D.keys():
...     print(key)
... 
a
b



>>> I = iter(D)
>>> I
<dict_keyiterator object at 0x7f5b39a358f0>
>>> next(I)
'a'
>>> next(I)
'b'
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

Range:
```
>>> R = range(5)
>>> R
range(0, 5)
>>> I = iter(R)

>>> I.__next__()
0
>>> I.__next__()
1
>>> next(I)
2
>>> next(I)
3
>>> next(I)
4
>>> next(I)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```
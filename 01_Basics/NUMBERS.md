# NUMBERS
(shell logs)

### BASICS
```
shtlp_0166@SHTLP0166:~/Documents/python_week/01_Basics$ python3
Python 3.10.12 (main, Feb  4 2025, 14:57:36) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> int(2.23)
2
>>> float(5)
5.0
>>> complex(1.2)
(1.2+0j)
>>> x = 1
>>> y = 2
>>> z = 3
>>> x, y, z
(1, 2, 3)
>>> x+1, y*2, z/4
(2, 4, 0.75)
>>> y % 3
2
>>> y
2
>>> z
3
>>> z ** 3
27
>>> 2 ** 1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
```
### Math: floor, trunc, etc
```
>>> import math
>>> math.floor(3.5)
3
>>> math.floor(-3.5)
-4
>>> math.trunc(-2.8) #towards zero always
-2
>>> math.trunc(2.8)
2
```

### Octal, Hexal Binaries
```
>>> 0o20 #Octal
16
>>> 0xFF #Hexal
255
>>> 0b1000 #Binary
8

>>> int('64',8) #octal value of 64
52
>>> int('10000',2) #Binary
16
>>> 
```

### BITWISE OPERATIONS
```
>>> x = 1
>>> x << 3 
8
>>> x
1
>>> x | 2
3
```

### Random
```
>>> import random
>>> random.random()
0.9435820236097089
>>> random.randint(1,100)
50
>>> random.choice(["option1", "option2", "option3"])
'option1'
>>> random.choice(["option1", "option2", "option3"])
'option2'
>>> l1 = ["option1", "option2", "option3"]
>>> random.shuffle(l1)
>>> l1
['option2', 'option3', 'option1']
```
###

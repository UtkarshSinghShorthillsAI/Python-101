# LISTS and LIST Operations


```
>>> Juices = ["Pomegranate", "Guava", "Grape", "Apple"]
>>> print(Juices)
['Pomegranate', 'Guava', 'Grape', 'Apple']
>>> print(Juices[2])
Grape
>>> print(Juices[2:4])
['Grape', 'Apple']
>>> Juices[3] = "Mango"
>>> print(Juices)
['Pomegranate', 'Guava', 'Grape', 'Mango']
>>> Juices[1:3] = ["Lemon", "Orange"]
>>> print(Juices)
['Pomegranate', 'Lemon', 'Orange', 'Mango']
>>> Juices[1:1]
[]
>>> Juices[1:1] = ["Grape", "Blueberry"]
>>> print(Juices)
['Pomegranate', 'Grape', 'Blueberry', 'Lemon', 'Orange', 'Mango']
>>> Juices[4:6] = []
>>> print(Juices)
['Pomegranate', 'Grape', 'Blueberry', 'Lemon']
>>> for juice in Juices:
...     print(juice)
... 
Pomegranate
Grape
Blueberry
Lemon
>>> for juice in Juices:
...     print(juice, end="+$+")
... 
Pomegranate+$+Grape+$+Blueberry+$+Lemon+$+>>> 
>>> if "Orange" in Juices: 
...     print("I have Orange juice")
... 
>>> if "Grape" in Juices: 
...     print("I have {} juice".format("Grape"))
... 
I have Grape juice
```

### Append
```
>>> Juices.append("Orange")
>>> print(Juices)
['Pomegranate', 'Grape', 'Blueberry', 'Lemon', 'Orange']
```

### Pop, remove
```
>>> Juices.remove("Orange")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> Juices.remove("Grape")
>>> print(Juices)
['Pomegranate', 'Blueberry', 'Lemon']
>>> 
```
### Insert at index

```
>>> Juices.insert(1,"Grape")
>>> print(Juices)
['Pomegranate', 'Grape', 'Blueberry', 'Lemon']
```
### Copying List (new reference)
```
>>> print(Juices)
['Pomegranate', 'Grape', 'Blueberry', 'Lemon']
>>> Juices_copy = Juices.copy()
>>> Juices_copy
['Pomegranate', 'Grape', 'Blueberry', 'Lemon']



>>> Juices.append("Apple")
>>> Juices_copy
['Pomegranate', 'Grape', 'Blueberry', 'Lemon']
>>> print(Juices)
['Pomegranate', 'Grape', 'Blueberry', 'Lemon', 'Apple']
```

### Misc.
```
>>> squared_nums = [x**2 for x in range (10)]
>>> squared_nums
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> cube_nums = [x**3 for x in range (10)]
>>> cube_nums
[0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
```
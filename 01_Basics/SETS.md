# Sets

### Creating
```
>>> myset = {"apple", "banana", "cherry", "apple"}
>>> print(myset)
{'cherry', 'banana', 'apple'}
```
### Checking membership
```
>>> print("banana" in myset) 
True
```
### Adding elements to set
```
>>> myset.add("guava")
>>> myset
{'cherry', 'guava', 'banana', 'apple'}


>>> myset.update(["pomegranate","orange"])
>>> myset
{'orange', 'pomegranate', 'apple', 'cherry', 'banana', 'guava'}
```

### Removing Elements
```
>>> myset.remove("banana")
>>> myset
{'orange', 'pomegranate', 'apple', 'cherry', 'guava'}

>>> # discard() does not raise an error if the element is not found
>>> myset.discard("grape")  # No error even though 'grape' is not in the set
```
### Set Operations
```
# UNION

>>> set1 = {"apple", "banana"}
>>> set2 = {"cherry", "banana"}
>>> result = set1.union(set2)
>>> print(result)
{'cherry', 'banana', 'apple'}



# INTERSECTION

>>> set1 = {"apple", "banana"}
>>> set2 = {"banana", "cherry"}
>>> result = set1.intersection(set2)
>>> print(result)  
{'banana'}



# DIFFERENCE

>>> set1 = {"apple", "banana", "cherry"}
>>> set2 = {"banana", "cherry"}
>>> result = set1.difference(set2)
>>> print(result)
{'apple'}


# LOOPING

>>> myset = {"apple", "banana", "cherry"}
>>> for item in myset:
...     print(item)
... 
cherry
banana
apple

```
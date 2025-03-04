# Tuples

```
>>> tea_types = ('Masala', 'Ginger', 'Green')
>>> tea_types
('Masala', 'Ginger', 'Green')
>>> type(tea_types)
<class 'tuple'>

>>> tea_types[0] = "Lemon"      #Immutable, hence this is not possible
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


# Adding two tuples

>>> more_tea = ('Herbal', 'Earl Grey')
>>> all_tea = more_tea + tea_types

>>> all_tea
('Herbal', 'Earl Grey', 'Masala', 'Ginger', 'Green')


>>> if "Herbal" in all_tea:
...     print("I have Herbal tea")
... 
I have Herbal tea
```

### Tuple Unpacking
```
>>> tea_types
('Masala', 'Ginger', 'Green')
>>> (msl, gngr, grn) = tea_types
>>> msl
'Masala'
>>> gngr
'Ginger'



>>> x = ('banana', 'apple', 'mango')
>>> b, *O = x
>>> b
'banana'
>>> O
['apple', 'mango']
```

### Updating Tuple
```
>>> x = ('banana', 'apple', 'mango')
>>> y = list(x)
>>> y
['banana', 'apple', 'mango']
>>> y[2] = 'grape'
>>> y
['banana', 'apple', 'grape']
>>> x = tuple(y)
>>> x
('banana', 'apple', 'grape')
```
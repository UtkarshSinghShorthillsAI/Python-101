
# DICTIONARY

```
>>> tea_types = {"Masala" : "Spicy", "Ginger":"Zesty", "green":"mild" }
>>> tea_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'green': 'mild'}
>>> tea_types['Masala']
'Spicy'
>>> tea_types['green'] = 'Fresh'
>>> tea_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'green': 'Fresh'}
```
### Iterating in Dictionary
```
>>> for tea in tea_types:
...     print(tea)
... 
Masala
Ginger
green


>>> for tea in tea_types:
...     print(tea,":", tea_types[tea])
... 
Masala : Spicy
Ginger : Zesty
green : Fresh


>>> for key, values in tea_types.items():
...     print(key, ":", "values")
... 
Masala : values
Ginger : values
green : values
```
### Adding a Key
```
>>> tea_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'green': 'Fresh'}
>>> tea_types["Earl Grey"] = "Citrus"
>>> tea_types
{'Masala': 'Spicy', 'Ginger': 'Zesty', 'green': 'Fresh', 'Earl Grey': 'Citrus'}
```

### Popping a Key
```
# by providing a key

>>> tea_types.pop("Masala")
'Spicy'
>>> tea_types
{'Ginger': 'Zesty', 'green': 'Fresh', 'Earl Grey': 'Citrus'}

# popping last key

>>> tea_types.popitem()
('Earl Grey', 'Citrus')
>>> tea_types
{'Ginger': 'Zesty', 'green': 'Fresh'}

# using del to delete a key

>>> del tea_types["green"]
>>> tea_types
{'Ginger': 'Zesty'}
```

### Copying Dictionary
```
>>> tea_types
{'Ginger': 'Zesty'}
>>> tea_types_copy = tea_types.copy()
>>> tea_types_copy
{'Ginger': 'Zesty'}
```

### Nested Dictionary
```
 >>> cafe = {
... "tea" : {"green" : "antioxidant", "oolong" : "floral", "matcha" : "earthy"},
... "coffee" : {"cappuccino" : "frothy", "espresso" : "strong", "americano":"diluted"}
... }


>>> print(cafe)
{'tea': {'green': 'antioxidant', 'oolong': 'floral', 'matcha': 'earthy'}, 'coffee': {'cappuccino': 'frothy', 'espresso': 'strong', 'americano': 'diluted'}}

>>> cafe["coffee"]
{'cappuccino': 'frothy', 'espresso': 'strong', 'americano': 'diluted'}


>>> cafe["coffee"]["espresso"]
'strong'


>>> squares = {x:x**2 for x in range(6)}
>>> squares
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

>>> squares.clear()
>>> squares
{}
```

### Dictionary fromkeys
```
>>> keys = ["espresso", "americano", "cappuccino"]
>>> default_value = "tasty"

>>> new_dict = dict.fromkeys(keys, default_value)
>>> new_dict
{'espresso': 'tasty', 'americano': 'tasty', 'cappuccino': 'tasty'}
```

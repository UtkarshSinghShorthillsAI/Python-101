# STRINGS

Basics, Slicing

```
>>> s1 = "Lemon tea"
>>> first_char = s1[0]      #Strings are treated as lists
>>> print(first_char)
L
>>> slice_s1 = s1[0:5]
>>> print(slice_s1)
Lemon
>>> 
>>> num_list = "0123456789"
>>> num_list[:]
'0123456789'
>>> num_list[:4]
'0123'
>>> num_list[5:]
'56789'
>>> num_list[2:8:2]
'246'
```

### Other Operations on Strings
```
>>> s1.lower()
'lemon tea'
>>> s1.upper()
'LEMON TEA'
>>> s2 = "    Cold Coffee    "
>>> s2
'    Cold Coffee    '
>>> print(s2.strip())
Cold Coffee
```

### Replace
```
>>> s3 = "Lemon Tea"
>>> s3
'Lemon Tea'
>>> print(s3.replace("Lemon","Ginger"))
Ginger Tea
>>> s3
'Lemon Tea'
```
### Split

```
>>> Tea = "Lemon, Ginger, Mint, Cinnamon"
>>> print(Tea.split(", "))
['Lemon', 'Ginger', 'Mint', 'Cinnamon']
```

### Find, Count, Format
```
>>> s5 = "Cinnamon Tea"
>>> s5.find("Tea")
9
>>> s5.find("Ginger")
-1                             #not found


>>> s6 = "Alpha beta gamma alpha beta alpha"
>>> s6.count("a")
9
>>> s6.count("alpha")
2
>>> 

>>> juice = "Apple"
>>> quantity = 2
>>> order = "I ordered {} glasses of {} juice"
>>> print(order.format(quantity, juice))
I ordered 2 glasses of Apple juice
>>> 
```

### list to string
```
>>> Juices = ["pomegranate","Apple","Mango","Orange"]
>>> Juices
['pomegranate', 'Apple', 'Mango', 'Orange']
>>> print(", ".join(Juices))
pomegranate, Apple, Mango, Orange
```
### Others

```
>>> juice = "He said \"This juice is awesome \""
>>> print(juice)
He said "This juice is awesome "


>>> juice = "I'm doing\nthis\ntonight"
>>> print(juice)
I'm doing
this
tonight
>>> print(r"I'm doing\nthis")    # to treat the string as raw
I'm doing\nthis
>>> 
```

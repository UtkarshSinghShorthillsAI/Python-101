from typing import Set


items = ["apple", "banana", "orange", "apple", "mango"]
unique_item: Set[str] = set()
for item in items:
    if item in unique_item:
        print(f"{item} is a duplicate")
        break
    unique_item.add(item)
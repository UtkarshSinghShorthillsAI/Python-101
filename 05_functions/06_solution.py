
from typing import Callable

cube: Callable[[int], int] = lambda x: x ** 3

print(cube(3))

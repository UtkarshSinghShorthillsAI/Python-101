from typing import Tuple

def area_circum(r: int) -> Tuple[float, float]:
    return (3.14 * r ** 2, 2 * 3.14 * r)

r = 5
a, c = area_circum(r)

print(f"Area: {a}, Circumference: {c} for radius {r}")
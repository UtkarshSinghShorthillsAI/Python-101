n = 100
orig = n
fact = 1

while n :
    fact *= n
    n -= 1

print(f"factorial of {orig} is {fact}")
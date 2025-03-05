n = 10
sum = 0
sum_even = 0

for i in range(1, n+1):
    sum += i
    if i % 2 == 0:
        sum_even += i

print(f"Sum of first {n} natural numbers: {sum}")
print(f"Sum of first {n} even numbers: {sum_even}")
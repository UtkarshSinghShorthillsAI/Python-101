n = 313
is_prime = True
for i in range(2, n):
    if n % i == 0:
        is_prime = False
        break

print(f"{n} is {'prime' if is_prime else 'not prime'}")

s = "Utkarsh"
reverse_s = ""

for i in range(len(s)-1, -1, -1):
    reverse_s += s[i]

print(f"Reverse of {s} is {reverse_s}")

for c in reverse_s:
    if c == reverse_s[0]:
        continue
    reverse_s = c + reverse_s

print(reverse_s) #expected output: UtkarshsrakU

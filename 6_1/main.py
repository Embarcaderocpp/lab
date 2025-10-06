import sys

def sequence(n):
    if n % 2 == 0:
        return n**2 + 1
    else:
        return n**2 + 2 * n

count = 15

for n in range(1, count + 1):
    a_n = sequence(n)
    print(f"a{n} = {a_n}")
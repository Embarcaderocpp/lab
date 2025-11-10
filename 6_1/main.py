import sys

def sequence(n):
    result = 0
    if n % 2 == 0:
        result =  n**2 + 1
    else:
        result = n**2 + 2 * n
    return result

count = 15

for n in range(1, count + 1):
    a_n = sequence(n)
    print(f"a{n} = {a_n}")
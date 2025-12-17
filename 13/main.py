numbers = set()
from math import sqrt

itr: int = int(sqrt(1000))+1

for n in range(1, itr):
    for m in range(1, itr):
        k = n*n + m*m
        if k > 1000:
            break
        numbers.add(k)

for k in numbers:
    print(f"{k:>4}")

import random
from max import max_of

n = int(input())
lo = int(input())
hi = int(input())
x = [None]*n

print(x)
for i in range(n):
    x[i] = random.randint(lo, hi)

print(x)
print(max_of(x))

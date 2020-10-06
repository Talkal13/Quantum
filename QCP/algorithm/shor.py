import random
from math import gcd


def shor(N):
    x = random.randint(2, N-1)

    fac = gcd(x, N)
    if (fac != 1):
        return (fac, int(N / fac))

    

print(shor(10))
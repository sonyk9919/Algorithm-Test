import sys

input = sys.stdin.readline

n = int(input())
k = int(input())

def factorize(n):
    factor = 2
    factors = []
    while (factor ** 2 <= n):
        while (n % factor == 0):
            factors.append(factor)
            n = n // factor
        factor += 1
    if n > 1:
        factors.append(n)
    return factors

counter = 1
for i in range(2, n + 1):
    if max(factorize(i)) <= k:
        counter += 1

print(counter)
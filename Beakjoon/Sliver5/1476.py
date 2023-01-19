import sys


input = sys.stdin.readline

E, S, M = map(int, input().split())

counter = 1
e, s, m = 1, 1, 1

while e != E or s != S or m != M:
    counter += 1
    if e < 15:
        e += 1
    else:
        e = 1
    
    if s < 28:
        s += 1
    else:
        s = 1

    if m < 19:
        m += 1
    else:
        m = 1

print(counter)
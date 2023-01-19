import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [[0 for i in range(101)] for i in range(101)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(x1, x2 + 1):
        for k in range(y1, y2 + 1):
            arr[j][k] += 1

count = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] > m:
            count += 1

print(count)
import sys
import math

input = sys.stdin.readline

n = list(map(int, input().strip()))

arr = [0] * 11
for i in n:
    if i == 6 or i == 9:
        arr[10] += 1
    else:
        arr[i] += 1

if arr.index(max(arr)) == 10:
    print(math.ceil(arr[10] / 2))
else:
    print(max(arr))
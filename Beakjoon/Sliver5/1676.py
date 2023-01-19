import sys

input = sys.stdin.readline

n = int(input())
m = 1
while n != 0:
    m *= n
    n -= 1

arr = list(str(m))

count = 0
for i in range(len(arr) - 1, -1, -1):
    if arr[i] == "0":
        count += 1
    else:
        break

print(count)
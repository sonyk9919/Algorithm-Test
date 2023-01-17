import sys

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(input().strip())

count = n
for word in arr:
    for j in range(len(word) - 1):
        if word[j] == word[j + 1]:
            continue
        elif word[j] in word[j + 1:]:
            count -= 1
            break

print(count)
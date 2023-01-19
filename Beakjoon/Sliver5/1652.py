import sys

input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(list(input().strip()))

countX = 0
countY = 0
for i in range(n):
    placeX = 0
    placeY = 0
    for j in range(n):
        if arr[i][j] == ".":
            placeX += 1
        else:
            if placeX >= 2:
                countX += 1
            placeX = 0
    if placeX >= 2:
        countX += 1

    for j in range(n):
        if arr[j][i] == ".":
            placeY += 1
        else:
            if placeY >= 2:
                countY += 1
            placeY = 0
    if placeY >= 2:
            countY += 1 
    

print(countX, countY)
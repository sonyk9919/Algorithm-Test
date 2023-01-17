import sys

input = sys.stdin.readline

path = []
for i in range(36):
    path.append(input().strip())

# eng, num
moving = [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

def moveKnight(point):
    ablePoint = []
    for i, j in moving:
        newPoint = chr(ord(point[0]) + i) + str(int(point[1]) + j)
        ablePoint.append(newPoint)
    
    return ablePoint

flag = False

movePath = []
for i in range(len(path)):
    
    if path[i] in movePath:
        flag = True
        break
    else:
        movePath.append(path[i])

    ablePoint = moveKnight(path[i])

    if i == len(path) - 1:
        if path[0] in ablePoint:
            break
        else:
            flag = True
            break
    
    if path[i + 1] in ablePoint:
        continue
    else:
        flag = True
        break

if flag:
    print("Invalid")
else:
    print("Valid")
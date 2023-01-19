import sys

input = sys.stdin.readline

n = int(input())
act = list(input().strip())

playMap = [["." for _ in range(n)] for i in range(n)]

point = [0, 0]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# Down, Up, Right, Left

for i in act:
    if i == "U":
        if point[0] + dx[1] < 0:
            continue
        if playMap[point[0]][point[1]] == "-":
            playMap[point[0]][point[1]] = "+"
        elif playMap[point[0]][point[1]] == "+":
            pass
        else:
            playMap[point[0]][point[1]] = "|"
        point[0] += dx[1]
        point[1] += dy[1]
        if playMap[point[0]][point[1]] == "-":
            playMap[point[0]][point[1]] = "+"
        elif playMap[point[0]][point[1]] == "+":
            pass
        else:
            playMap[point[0]][point[1]] = "|"
    elif i == "D":
        if point[0] + dx[0] >= n:
            continue
        if playMap[point[0]][point[1]] == "-":
            playMap[point[0]][point[1]] = "+"
        elif playMap[point[0]][point[1]] == "+":
            pass
        else:
            playMap[point[0]][point[1]] = "|"
        point[0] += dx[0]
        point[1] += dy[0]
        if playMap[point[0]][point[1]] == "-":
            playMap[point[0]][point[1]] = "+"
        elif playMap[point[0]][point[1]] == "+":
            pass
        else:
            playMap[point[0]][point[1]] = "|"
    elif i == "L":
        if point[1] + dy[3] < 0:
            continue
        if playMap[point[0]][point[1]] == "|":
           playMap[point[0]][point[1]] = "+"
        elif playMap[point[0]][point[1]] == "+":
            pass
        else:
            playMap[point[0]][point[1]] = "-"
        point[0] += dx[3]
        point[1] += dy[3]
        if playMap[point[0]][point[1]] == "|":
           playMap[point[0]][point[1]] = "+"
        elif playMap[point[0]][point[1]] == "+":
            pass
        else:
            playMap[point[0]][point[1]] = "-"
    elif i == "R":
        if point[1] + dy[2] >= n:
            continue
        if playMap[point[0]][point[1]] == "|":
           playMap[point[0]][point[1]] = "+"
        elif playMap[point[0]][point[1]] == "+":
            pass
        else:
            playMap[point[0]][point[1]] = "-"
        point[0] += dx[2]
        point[1] += dy[2]
        if playMap[point[0]][point[1]] == "|":
           playMap[point[0]][point[1]] = "+"
        elif playMap[point[0]][point[1]] == "+":
            pass
        else:
            playMap[point[0]][point[1]] = "-"

for i in range(len(playMap)):
    for j in range(len(playMap)):
        print(playMap[i][j], end="")
    print("")
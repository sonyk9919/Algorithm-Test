import sys

input = sys.stdin.readline

def getWhoNegative(now, back, len):
    idx = now - back
    if idx < 0:
        idx += len
    return idx

number = 1
while True:
    n = int(input())
    if (n == 0): break

    flag = False
    arr = []
    for i in range(n):
        student = list(input().split())
        arr.append(student)
    
    print("Group", number)
    for i in range(len(arr)):
        for j in range(len(arr[i]) - 1):
            if arr[i][j + 1] == "N":
                flag = True
                idx = getWhoNegative(i, j + 1, len(arr))
                print(arr[idx][0], "was nasty about", arr[i][0])

    if flag == False:
        print("Nobody was nasty")
    
    print("")
    number += 1
    
    
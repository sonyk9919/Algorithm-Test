import sys

input = sys.stdin.readline

number = 1
while True:
    n = int(input())
    m = 2 * n - 1
    if (n == 0): break
    
    student = []
    take = []
    
    for i in range(n):
        student.append(input())
    
    for i in range(m):
        stu, dum = input().split()
        idx = int(stu) - 1
        if student[idx] in take:
            take.remove(student[idx])
        else:
            take.append(student[idx])

    print(number, end="")
    for i in take:
        print("", i, end="")
    
    number += 1
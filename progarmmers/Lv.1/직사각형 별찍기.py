a, b = map(int, input().strip().split(' '))

arr = [["*" for i in range(a)] for i in range(b)]

for i in range(b):
    print("".join(arr[i]))
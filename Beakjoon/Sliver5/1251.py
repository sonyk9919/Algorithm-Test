import sys

input = sys.stdin.readline

str = input()
strList = list(str)
result = []

for i in range(1, len(strList) - 2):
    for j in range(i + 1, len(strList) - 1):
        str1 = strList[0:i]
        str2 = strList[i:j]
        str3 = strList[j: len(strList) - 1]
        
        str1.reverse()
        str2.reverse()
        str3.reverse()

        sumList = str1 + str2 + str3
        result.append("".join(sumList))

result.sort()
print(result[0])
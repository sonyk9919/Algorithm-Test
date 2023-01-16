import sys

input = sys.stdin.readline

target = int(input())

List = [64]

while sum(List) > target:
    total = sum(List)
    minValue = min(List)
    List.remove(minValue)
    half = minValue // 2
    if total - half > target:
        List.append(half)
    else:
        List.append(half)
        List.append(half)

List.sort()
if List[0] == 0:
    List.remove(0)
    
print(len(List))

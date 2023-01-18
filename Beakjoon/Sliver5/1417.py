import sys

# 1. 값을 입력 받는다.
# 2. 1 ~ n - 1 까지 arr를 슬라이싱한다.
# 3. 슬라이싱한 arr에서 최댓값을 찾고 다솜이의 값과 비교한다
# 4. 비교하여 다솜이가 크다면 값을 출력하고 그렇지 않다면 Counter를 1증가시키고 최댓값을 1감소시킨다
# 5. 위의 과정을 반복한다.

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input().strip()))


dasom = arr[0]
candidate = arr[1:]
counter = 0
while len(candidate) != 0 and dasom <= max(candidate):
    idx = candidate.index(max(candidate))
    candidate[idx] -= 1
    dasom += 1
    counter += 1

print(counter)

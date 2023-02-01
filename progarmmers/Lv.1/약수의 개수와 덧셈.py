def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        arr = []
        for j in range(1, int(i ** 0.5) + 1):
            if i % j == 0:
                arr.append(j)
                arr.append(i / j)
        arr = list(set(arr))
        if len(arr) % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer
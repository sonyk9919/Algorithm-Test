def solution(s):
    answer = []
    for i in range(0, len(s)):
        target = i
        for j in range(0, i):
            if s[j] == s[i]:
                target = j
        if target == i:
            answer.append(-1)
        else:
            answer.append(i - target)
    return answer
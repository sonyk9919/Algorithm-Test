def solution(k, score):
    answer = []
    day = []
    for i in range(0, len(score)):
        day.append(score[i])
        day.sort()
        if len(day) < k:
            answer.append(min(day))
        else:
            answer.append(min(day[len(day) - k:len(day)]))
    return answer
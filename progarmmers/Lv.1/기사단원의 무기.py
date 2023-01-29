def solution(number, limit, power):
    answer = 0
    Divisor = []
    for i in range(1, number + 1):
        counter = []
        for j in range(1, int(i ** (1 / 2)) + 1):
            if i % j == 0:
                counter.append(j)
                counter.append(i // j)
        
        Divisor.append(len(list(set(counter))))
    
    result = []
    for i in Divisor:
        if i > limit:
            result.append(power)
        else:
            result.append(i)
    
    answer = sum(result)
    return answer

    
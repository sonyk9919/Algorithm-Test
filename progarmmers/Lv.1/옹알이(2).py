def solution(babbling):
    answer = 0
    able = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        for j in able:
            if j * 2 not in i:
                i = i.replace(j, " ")
        
        if len(i.strip()) == 0:
            answer += 1
        
    return answer
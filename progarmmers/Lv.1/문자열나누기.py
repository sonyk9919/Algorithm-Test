def solution(s):
    answer = 0
    x = s[0]
    xx = 0
    xo = 0
    for i in s:
        if xx == 0 and xo == 0:
            x = i
            
        if x == i:
            xo += 1
        else:
            xx += 1
        
        if xx == xo:
            xx = xo = 0
            answer += 1
    
    if xx != 0 or xo != 0:
        answer += 1
        
    return answer
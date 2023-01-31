def solution(X, Y):
    answer = ''
    
    num_X = [X.count(str(i)) for i in range(10)] 
    num_Y = [Y.count(str(i)) for i in range(10)]
        
    for i in range(9, -1, -1):
        n = min(num_X[i], num_Y[i])
        answer += str(i) * n
        
    
    if answer == "":
        return "-1"
    if len(answer) == answer.count("0"):
        return "0"
    
    return answer
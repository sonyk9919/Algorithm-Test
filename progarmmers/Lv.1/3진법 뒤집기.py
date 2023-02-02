def solution(n):
    answer = 0
    arr = []
    
    while n > 0:
        arr.append(n % 3)
        n = n // 3
    
    for i in range(len(arr)):
        answer += arr.pop() * 3 ** i
        
    return answer
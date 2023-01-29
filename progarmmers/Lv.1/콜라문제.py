def solution(a, b, n):
    answer = 0
    while n >= a:
        add = b * (n // a)
        n = n % a
        n += add
        answer += add
    return answer
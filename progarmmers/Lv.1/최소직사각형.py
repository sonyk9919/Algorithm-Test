def solution(sizes):
    answer = 0
    row = 0
    col = 0
    for i in sizes:
        if i[0] > i[1]:
            row = max(row, i[0])
            col = max(col, i[1])
        else:
            row = max(row, i[1])
            col = max(col, i[0])
    
    answer = row * col
    return answer
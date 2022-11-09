def solution(num_list, n):
    answer = []
    col=n
    row=len(num_list)//n
    for i in range(row):
        cols=[]
        for j in range(col):
            cols.append(num_list[n*i+j])
        answer.append(cols)
    return answer
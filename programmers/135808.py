def solution(k, m, score):
    answer = 0
    score.sort()
    p=len(score)-m
    while p>-1:
        answer+=(score[p]*m)
        p-=m
    return answer
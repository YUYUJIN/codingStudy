def solution(a, b, n):
    answer=0
    remain=n
    
    while remain>=a:
        add=(int(remain/a))*b
        remain-=(int(remain/a))*a
        remain+=add
        answer+=add
    
    return answer
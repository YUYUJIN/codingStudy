def solution(s):
    answer = True
    opens=0
    
    for c in s:
        if c=='(':
            opens+=1
        else:
            opens-=1
            if opens<0:
                answer=False
    if opens>0:
        answer=False
    return answer
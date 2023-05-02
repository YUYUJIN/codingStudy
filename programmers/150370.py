def toDay(YMD):
    day=int(YMD[:4])*12*28
    day+=int(YMD[5:7])*28
    day+=int(YMD[8:])
    return day
    
def solution(today, terms, privacies):
    answer = []
    category=dict()
    for t in terms:
        category[t[:1]]=int(t[2:])*28
        
    td=toDay(today)
    for i,p in enumerate(privacies):
        if (toDay(p[:10])+category[p[11:]])<=td:
            answer.append(i+1)
    
    return answer
def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    
    losts=dict()
    for l in lost:
        losts[l]=1
    reserves=dict()
    for r in reserve:
        reserves[r]=1
    
    bring=[]
    for l in losts:
        if reserves.get(l):
            bring.append(l)
    for b in bring:
        del reserves[b]
        del losts[b]
    
    serve=len(losts)
    for r in reserves:
        if losts.get(r-1):
            serve-=1
            del losts[r-1]
        elif losts.get(r+1):
            serve-=1
            del losts[r+1]
        
    answer-=serve
            
    return answer
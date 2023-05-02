from heapq import heappop,heappush

def solution(scoville, K):
    answer = 0
    hq=[]
    for sc in scoville:
        heappush(hq,sc)
    
    sc1=heappop(hq)
    sc2=heappop(hq)
    while sc1<K:
        answer+=1
        heappush(hq,(sc1+(sc2*2)))
        if len(hq)==1:
            sc1=heappop(hq)
            if sc1<K:
                answer=-1
                break
        else:
            sc1=heappop(hq)
            sc2=heappop(hq)
        
    return answer
from collections import deque 

def solution(x, y, n):
    answer = 0
    dist=[0]*1000001
    
    dist[x]=1
    dq=deque()
    dq.append(x)
    while dq:
        t=dq.popleft()
        if t>y:
            continue
        if t==y:
            break
        if t+n<=1000001 and dist[t+n]==0:
            dist[t+n]=dist[t]+1
            dq.append(t+n)
        if t*2<=1000001 and dist[t*2]==0:
            dist[t*2]=dist[t]+1
            dq.append(t*2)
        if t*3<=1000001 and dist[t*3]==0:
            dist[t*3]=dist[t]+1
            dq.append(t*3)
            
    answer=dist[y]-1
    return answer
from heapq import heappop,heappush

def solution(jobs):
    answer = 0
    jobsq=[]
    readyq=[]
    
    for j in jobs:
        heappush(jobsq,(j[0],j))
    
    runtime=[]
    time=0
    while len(jobsq)>0:
        ready=jobsq[0][0]
        while ready<=time:
            job=heappop(jobsq)
            heappush(readyq,(job[1][1],job[1]))
            if len(jobsq)>0:
                ready=jobsq[0][0]
            else:
                break
        if len(readyq)>0:
            run=heappop(readyq)
            time+=run[0]
            runtime.append(time-run[1][0])
        else:
            time+=1
    
    while len(readyq)>0:
        if readyq[0][1][0]<=time:
            run=heappop(readyq)
            time+=run[0]
            runtime.append(time-run[1][0])
        else:
            time+=1
    answer=int(sum(runtime)/len(jobs))
    return answer
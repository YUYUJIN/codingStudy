import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    deploy_days=deque()
    for i in range(len(progresses)):
        day=math.ceil((100-progresses[i])/speeds[i])
        deploy_days.append(day)
        
    previous_process=0
    num_process=1
    while deploy_days:
        current_process=deploy_days.popleft()
        if previous_process<current_process:
            answer.append(num_process)
            previous_process=current_process
            num_process=1
        else:
            num_process+=1
    answer.append(num_process)
    return answer[1:]
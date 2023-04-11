from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting=deque(truck_weights)
    bridge=deque([0]*bridge_length)
    done=[]
    current_weight=0
    time=0
    while waiting:
        pass_truck=bridge.popleft()
        if pass_truck>0:
            current_weight-=pass_truck
            done.append(pass_truck)
        new_weight=waiting.popleft()
        if current_weight+new_weight<=weight:
            current_weight+=new_weight
            bridge.append(new_weight)
        else:
            bridge.append(0)
            waiting.appendleft(new_weight)
        time+=1
    while bridge:
        pass_truck=bridge.popleft()
        if pass_truck>0:
            current_weight-=pass_truck
            done.append(pass_truck)
        time+=1
    answer=time
    return answer
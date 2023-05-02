def solution(priorities, location):
    answer = 0
    while True:
        prin=True
        j=priorities.pop(0)
        for p in priorities:
            if j<p:
                prin=False
        if prin:
            answer+=1
            if location==0:
                break
        else:
            priorities.append(j)
        location-=1
        if location<0:
            location=len(priorities)-1
        
    return answer
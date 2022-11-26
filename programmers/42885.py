from collections import deque

def solution(people, limit):
    answer = 0
    remainPeople=deque(sorted(people))
    while len(remainPeople)>0:
        boat=limit
        boat-=remainPeople.pop()
        if len(remainPeople)>0:
            if boat>=remainPeople[0]:
                remainPeople.popleft()
        answer+=1
    return answer
def solution(participant, completion):
    answer = ''
    participantSorted=sorted(participant)
    completionSorted=sorted(completion)
    completionSorted.append("test")
    
    for i in range(len(participant)):
        if participantSorted[i] != completionSorted[i]:
            answer=participantSorted[i]
            break
            
    return answer
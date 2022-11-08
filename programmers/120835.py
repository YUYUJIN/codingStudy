def solution(emergency):
    answer = [0 for i in range(len(emergency))]
    for i in range(len(emergency)):
        count=1
        for j in range(len(emergency)):
            if emergency[i]<emergency[j]:
                count+=1
        answer[i]=count
    return answer
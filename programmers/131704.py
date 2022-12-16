def solution(order):
    answer = 0
    otherConveyor=[0]
    
    mainConveyor=1
    while mainConveyor<len(order)+1:
        if mainConveyor==order[answer]:
            answer+=1
            mainConveyor+=1
        elif otherConveyor[-1]==order[answer]:
                answer+=1
                otherConveyor.pop(-1)
        else:
            otherConveyor.append(mainConveyor)
            mainConveyor+=1
    while len(otherConveyor)>1:
        if otherConveyor.pop(-1)==order[answer]:
            answer+=1
        else:
            break
    return answer
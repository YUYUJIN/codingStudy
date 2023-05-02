def solution(prices):
    answer = []
    for i in range(len(prices)):
        maintain=0
        for j in range(i+1,len(prices)):
            maintain+=1
            if prices[i]>prices[j]:
                break
        answer.append(maintain)
    return answer
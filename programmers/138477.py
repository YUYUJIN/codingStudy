def solution(k, score):
    answer = [score[0]]
    rank=[score[0]]
    for i in range(1,len(score)):
        for j in range(len(rank)):
            if rank[j]<score[i]:
                rank.insert(j,score[i])
                break
        if j==(len(rank)-1):
            rank.append(score[i])
        
        if i<k:
            answer.append(rank[-1])
        else:
            answer.append(rank[k-1])
            
    return answer
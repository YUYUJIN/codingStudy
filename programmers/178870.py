def solution(sequence, k):
    answer = []
    answer_len=1000001
    
    
    subSet=[]
    idx=0
    sums=0
    for i in range(len(sequence)-1,-1,-1):
        if sequence[i]>k:
            continue
        subSet.append(sequence[i])
        sums+=sequence[i]
        if sums>k:
            sums-=subSet[idx]
            idx+=1
        if sums==k:
            if (len(subSet)-idx-1)<=answer_len:
                answer_len=(len(subSet)-idx-1)
                answer=[i,i+(len(subSet)-idx-1)]
            
    return answer
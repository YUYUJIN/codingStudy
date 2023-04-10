def solution(players, callings):
    answer = []
    rank=dict()
    rank_rev=dict()
    for i,p in enumerate(players):
        rank[p]=i+1
        rank_rev[i+1]=p
    
    for c in callings:
        rank[c]-=1
        up=rank[c]
        back=rank_rev[up]
        rank[back]+=1
        rank_rev[up]=c
        rank_rev[up+1]=back
    
    for i in rank_rev.keys():
        answer.append(rank_rev[i])
    return answer
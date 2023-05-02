def solution(n, computers):
    answer = len(computers)
    done=dict()
    
    
    for i,com in enumerate(computers):
        stack=[i]
        done[i]=1
        while len(stack)>0:
            com=computers[stack.pop()]
            for j,c in enumerate(com):
                if c==1 and not done.get(j):
                    stack.append(j)
                    done[j]=1
                    answer-=1
    return answer
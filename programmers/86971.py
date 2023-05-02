def turnoff(tower,done,edges,node):
    target=edges[node]
    tower[node-1]=0
    done[node]=1
    for t in target:
        if done.get(t):
            continue
        tower[t-1]=0
        done[t]=1
        tower=turnoff(tower,done,edges,t)
    return tower

def solution(n, wires):
    answer = 100
    edges={w+1:[] for w in range(n)}
    for wire in wires:
        edges[wire[0]].append(wire[1])
        edges[wire[1]].append(wire[0])
    
    for wire in wires:
        tower=[1 for i in range(n)]
        done={wire[1]:1}
        tower=turnoff(tower,done,edges,wire[0])
        one=sum(tower)
        two=n-sum(tower)
        case=abs(one-two)
        if answer>case:
            answer=case
    return answer
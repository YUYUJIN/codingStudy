def search(a,nodes):
    if nodes[a]==a: 
        return a
    else:
        nodes[a]=search(nodes[a],nodes)
        return nodes[a]
    

def solution(n, costs):
    answer = 0
    nodes=dict()
    side=0
    for i in range(n):
        nodes[i]=i
    costs.sort(key=lambda x:x[2])
    
    for c in costs:
        search(c[0],nodes)
        search(c[1],nodes)
        if nodes[c[0]]==nodes[c[1]]:
            continue
        if nodes[c[0]]>nodes[c[1]]:
            nodes[nodes[c[0]]]=nodes[c[1]]
            nodes[c[0]]=nodes[c[1]]
        else:
            nodes[nodes[c[1]]]=nodes[c[0]]
            nodes[c[1]]=nodes[c[0]]  
        answer+=c[2]
        side+=1
        if side==(n-1):
            break
        
    return answer
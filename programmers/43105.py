def solution(triangle):
    answer = 0
    tree=triangle
    for i in range(1,len(tree)):
        for j in range(i+1):
            if j==0:
                tree[i][j]+=tree[i-1][0]
            elif j==i:
                tree[i][j]+=tree[i-1][j-1]
            else:
                left=tree[i-1][j-1]
                right=tree[i-1][j]
                if left>=right:
                    tree[i][j]+=left
                else:
                    tree[i][j]+=right
    
    coordinate=tree[len(tree)-1]
    for c in coordinate:
        if answer<c:
            answer=c
        
    return answer
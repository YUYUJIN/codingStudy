def updownleftright(i,j,width,height,visited,maps):
    result=[]
    if i-1>=0 : 
        if visited[i-1][j]==0 and maps[i-1][j]!='X': result.append([i-1,j]) 
    if i+1<height :
        if visited[i+1][j]==0 and maps[i+1][j]!='X': result.append([i+1,j]) 
    if j-1>=0 : 
        if visited[i][j-1]==0 and maps[i][j-1]!='X': result.append([i,j-1]) 
    if j+1<width :
        if visited[i][j+1]==0 and maps[i][j+1]!='X': result.append([i,j+1]) 
    
    return result

def solution(maps):
    answer = []
    width=len(maps[0])
    height=len(maps)
    visited=[[0 for i in range(width)] for j in range(height)]
    
    for y in range(len(maps)):
        for x in range(len(maps[y])):
            if visited[y][x]==1:
                continue
            visited[y][x]=1
            if maps[y][x]=='X':
                continue
            
            queue=[]
            land=int(maps[y][x])
            queue+=updownleftright(y,x,width,height,visited,maps)
            while len(queue)>0:
                cor=queue.pop()
                if visited[cor[0]][cor[1]]==1:
                    continue
                t=maps[cor[0]][cor[1]]
                visited[cor[0]][cor[1]]=1
                if t=='X':
                    continue
                land+=int(t)
                queue+=updownleftright(cor[0],cor[1],width,height,visited,maps)
            answer.append(land)
            
    if len(answer)==0:
        answer=[-1]
    else:
        answer.sort()
    return answer
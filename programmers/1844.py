def isValidPass(maps,x,y):
    n=len(maps)
    m=len(maps[0])
    
    if y>-1 and y<n and x>-1 and x<m:
        if maps[y][x]:
            return True
    return False
        
def checkPass(maps,y,x,passMap):
    result=[]
    if isValidPass(maps,x+1,y):
        if passMap[y][x+1]<0:
            passMap[y][x+1]=passMap[y][x]+1
            result.append([y,x+1])
    if isValidPass(maps,x-1,y):
        if passMap[y][x-1]<0:
            passMap[y][x-1]=passMap[y][x]+1
            result.append([y,x-1])
    if isValidPass(maps,x,y+1):
        if passMap[y+1][x]<0:
            passMap[y+1][x]=passMap[y][x]+1
            result.append([y+1,x])
    if isValidPass(maps,x,y-1):
        if passMap[y-1][x]<0:
            passMap[y-1][x]=passMap[y][x]+1
            result.append([y-1,x])
    return result

def BFS(maps,passMap):
    y,x=0,0
    queue=checkPass(maps,y,x,passMap)
    
    while len(queue)>0:
        py,px=queue.pop(0)
        queue.extend(checkPass(maps,py,px,passMap))
        
def solution(maps):
    n=len(maps)
    m=len(maps[0])
    passMap=[[-1 for i in range(m)] for i in range(n)]
    passMap[0][0]=1
    
    BFS(maps,passMap)
    
    return passMap[n-1][m-1]
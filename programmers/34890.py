def starpoint(line1,line2):
    a,b,e=line1
    c,d,f=line2
    if (a*d)-(b*c)==0:
        return False,(0,0)
    
    x=(((b*f)-(e*d))/((a*d)-(b*c)))
    y=(((e*c)-(a*f))/((a*d)-(b*c)))
    if int(x)==x and int(y)==y:
        return True,(int(x),int(y))
    else:
        return False,(0,0)

def solution(line):
    answer = []
    point=[]
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            check,p=starpoint(line[i],line[j])
            if check:
                point.append(p)
    
    maxx=point[0][0]
    maxy=point[0][1]
    minx=point[0][0]
    miny=point[0][1]
    for p in point:
        maxx=max(maxx,p[0])
        minx=min(minx,p[0])
        maxy=max(maxy,p[1])
        miny=min(miny,p[1])
    
    width=maxx-minx+1
    height=maxy-miny+1
    maps=[]
    for h in range(height):
        xasix=[]
        for w in range(width):
            xasix.append('.')
        maps.append(xasix)
        
    for x,y in point:
        maps[y-miny][x-minx]='*'
    
    for i in range(len(maps)-1,-1,-1):
        answer.append(''.join(x for x in maps[i]))
        
    return answer
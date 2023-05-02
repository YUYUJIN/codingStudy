def solution(X, Y):
    answer = ''
    xd=dict()
    yd=dict()
    for x in X:
        if xd.get(x):
            xd[x]+=1
        else:
            xd[x]=1
    for y in Y:
        if yd.get(y):
            yd[y]+=1
        else:
            yd[y]=1
    num=[]
    for x in xd:
        if yd.get(x):
            mn=min(xd[x],yd[x])
            for i in range(mn):
                num.append(x)
    
    num.sort(key=lambda x:-ord(x))
    if len(num)>0:
        if num[0]=='0':
            answer='0'
        else:
            answer=''.join(num)
    else:
        answer='-1'        
    return answer
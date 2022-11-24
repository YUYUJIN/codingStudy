import sys

n=int(sys.stdin.readline())
x=[]

s=sys.stdin.readline().split('\n')[0].split(' ')
for i in range(n):
    x.append([int(s[i]),i])

x=sorted(x,key=lambda x:x[0])

newX=0
currentMinX=x[0][0]
x[0][0]=0
for i in range(1,n):
    if x[i][0]>currentMinX:
        newX+=1
        currentMinX=x[i][0]
    x[i][0]=newX

x=sorted(x,key=lambda x:x[1])

for i in range(n):
    print(x[i][0],end=' ')
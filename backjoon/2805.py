import sys

n,m=map(int,sys.stdin.readline().split('\n')[0].split())

trees=list(map(int,sys.stdin.readline().split('\n')[0].split()))

minM,maxM=0,max(trees)

result=0
while(minM<=maxM):
    resultM=0
    p=(maxM+minM)//2
    for t in trees:
        if t>=p:
            resultM+=t-p
    if resultM<m:
        maxM=p-1
    else:
        result=p
        minM=p+1

print(result)
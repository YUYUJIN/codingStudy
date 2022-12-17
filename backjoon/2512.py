import sys

n=int(sys.stdin.readline())
localR=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())

minM=0
maxM=max(localR)
answer=0
while minM<=maxM:
    targetM=(maxM+minM)//2
    
    sumM=0
    for i in localR:
        if targetM>i:
            sumM+=i
        else:
            sumM+=targetM
    
    if sumM>m:
        maxM=targetM-1
    else:
        minM=targetM+1
        if answer<sumM:
            answer=targetM

print(answer)

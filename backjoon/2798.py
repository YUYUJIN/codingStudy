import sys

n,m=map(int,sys.stdin.readline().split('\n')[0].split())
num=list(map(int,sys.stdin.readline().split('\n')[0].split()))

bestSum=0
bestLoss=100000000
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            candidate=num[i]+num[j]+num[k]
            loss=abs(m-candidate)
            if loss<bestLoss:
                bestSum=candidate
                bestLoss=loss

print(bestSum)
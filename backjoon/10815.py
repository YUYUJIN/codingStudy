import sys

n=int(sys.stdin.readline())
ans=set(map(int,sys.stdin.readline().split('\n')[0].split()))

m=int(sys.stdin.readline())
num=list(map(int,sys.stdin.readline().split('\n')[0].split()))

res=[]
for i in range(m):
    if num[i] in ans:
        res.append(1)
    else:
        res.append(0)

print(' '.join(str(_) for _ in res))
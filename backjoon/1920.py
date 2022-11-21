import sys

def search(m,A):
    low=0
    high=len(A)-1
    while low<=high:
        p=low+((high-low)//2)
        if A[p]==m:
            return 1
        elif A[p]>m:
            high=p-1
        else:
            low=p+1
    return 0

n=int(sys.stdin.readline())
As=sys.stdin.readline().split(' ')
A=[]
for i in range(n):
    A.append(int(As[i]))
m=int(sys.stdin.readline())
Ms=sys.stdin.readline().split(' ')
M=[]
for i in range(m):
    M.append(int(Ms[i]))

ans=[]
A.sort()

for i in M:
    ans.append(search(i,A))

for i in ans:
    print(i,end=' ')
    

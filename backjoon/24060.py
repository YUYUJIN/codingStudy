import sys

def merge_sort(A,p,r,n_k):
    if p<r:
        q=(p+r)//2
        merge_sort(A,p,q,n_k)
        merge_sort(A,q+1,r,n_k)
        merge(A,p,q,r,n_k)

def merge(A,p,q,r,n_k):
    i,j=p,q+1
    tmp=[]
    while i<=q and j <= r:
        if A[i]<=A[j]:
            tmp.append(A[i])
            i+=1
        else:
            tmp.append(A[j])
            j+=1
    while i<=q:
        tmp.append(A[i])
        i+=1
    while j<=r:
        tmp.append(A[j])
        j+=1
    i,t=p,0
    while i<=r:
        n_k.append(tmp[t])
        A[i]=tmp[t]
        i+=1
        t+=1

n,k=map(int,sys.stdin.readline().split('\n')[0].split(' '))
A=list(map(int,sys.stdin.readline().split('\n')[0].split(' ')))
n_k=[]
merge_sort(A,0,n-1,n_k)
if len(n_k)<=k:
    print(-1)
else:
    print(n_k[k-1])
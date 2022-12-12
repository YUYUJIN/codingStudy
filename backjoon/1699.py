import sys
import math

n=int(sys.stdin.readline())

degree=[]
for i in range(n+1):
    degree.append(i)

for i in range(4,n+1):
    j=1
    for j in range(1,int(math.sqrt(i)+1)):
        if degree[i-j**2]+1<degree[i]:
            degree[i]=degree[i-j**2]+1

print(degree[n])
import sys

n=int(sys.stdin.readline())
ps=sys.stdin.readline().split(' ')
p=[]
for i in range(n):
    p.append(int(ps[i]))

p.sort()

result=0
for i in range(n):
    result+=p[i]*(n-i)

print(result)
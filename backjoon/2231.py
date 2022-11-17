import sys

num=int(sys.stdin.readline())

result=0
for i in range(1,num):
    N=i
    si=str(i)
    for j in si:
        N+=int(j)
    if num==N:
        result=i
        break

print(result)
import sys

n=int(sys.stdin.readline())
mans=[]

for i in range(n):
    mans.append(tuple(map(int,sys.stdin.readline().split('\n')[0].split())))

rank=[]
for i in range(n):
    count=1
    for j in range(n):
        if i==j:
            continue
        elif mans[i][0]<mans[j][0] and mans[i][1]<mans[j][1]:
            count+=1
    rank.append(count)

for i in range(n):
    print(rank[i],end=' ')
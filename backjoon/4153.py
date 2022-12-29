import sys

answer=[]
while True:
    lineSize=list(map(int,sys.stdin.readline().split()))
    if sum(lineSize)<1:
        break
    else:
        lineSize.sort()
        if lineSize[0]**2+lineSize[1]**2==lineSize[2]**2:
            answer.append('right')
        else:
            answer.append('wrong')

for i in answer:
    print(i)
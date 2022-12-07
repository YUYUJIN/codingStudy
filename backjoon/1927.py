import sys
from queue import PriorityQueue

n=int(sys.stdin.readline().split('\n')[0])

minHeap=PriorityQueue()
printNum=[]
for i in range(n):
    x=int(sys.stdin.readline().split('\n')[0])
    if x==0:
        if minHeap.qsize()<1:
            printNum.append(0)
        else:
            printNum.append(minHeap.get())
    else:
        minHeap.put(x)

for i in range(len(printNum)):
    print(printNum[i])

    
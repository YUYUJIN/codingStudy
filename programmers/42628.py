from heapq import heappop,heappush

def popUtil(heap,datanote):
    while len(heap)>0:
        val=heappop(heap)[1]
        if datanote.get(val):
            if datanote[val]>1:
                datanote[val]-=1
            else:
                del datanote[val]
            return val
    return 0
    

def solution(operations):
    answer = []
    maxheap=[]
    minheap=[]
    datanote=dict()
    
    for op in operations:
        if op[0]=='I':
            value=int(op[2:])
            heappush(maxheap,(-value,value))
            heappush(minheap,(value,value))
            if datanote.get(value):
                datanote[value]+=1
            else:
                datanote[value]=1
        else:
            if op[2:]=='1':
                popUtil(maxheap,datanote)
            elif op[2:]=='-1':
                popUtil(minheap,datanote)
    answer=[popUtil(maxheap,datanote),popUtil(minheap,datanote)]
    return answer
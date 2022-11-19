import sys

def DFS(edges,v):
    print(v,end=' ')
    stack=list(reversed(edges[v-1]))
    complete=[False]*(len(edges))
    complete[v-1]=True

    while len(stack)>0:
        vertex=stack.pop(len(stack)-1)
        if complete[vertex-1]:
            continue
        stack.extend(list(reversed(edges[vertex-1])))
        complete[vertex-1]=True
        print(vertex,end=' ')

def BFS(edges,v):
    print(v,end=' ')
    queue=edges[v-1]
    complete=[False]*(len(edges))
    complete[v-1]=True

    while len(queue)>0:
        vertex=queue.pop(0)
        if complete[vertex-1]:
            continue
        queue.extend(edges[vertex-1])
        complete[vertex-1]=True
        print(vertex,end=' ')
    
n,m,v=map(int,sys.stdin.readline().split('\n')[0].split(' '))

edges=[[] for i in range(n)]
for i in range(m):
    vertex,edge=map(int,sys.stdin.readline().split('\n')[0].split(' '))
    edges[vertex-1].append(edge)
    edges[edge-1].append(vertex)  #양방향

for i in range(len(edges)):
    #중복제거, 정렬
    edges[i]=list(set(edges[i]))
    edges[i].sort()  

DFS(edges,v)
print()
BFS(edges,v)

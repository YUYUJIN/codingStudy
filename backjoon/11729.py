import sys

def hanoi(n,start,mid,end,move):
    if(n==1):
        move.append('{} {}'.format(start,end))
    else:
        hanoi(n-1,start,end,mid,move)
        move.append('{} {}'.format(start,end))
        hanoi(n-1,mid,start,end,move)

n=int(sys.stdin.readline().split()[0])

move=[]
hanoi(n,1,2,3,move)
print(len(move))
for s in move:
    print(s)
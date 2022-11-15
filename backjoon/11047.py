import sys

inputs=sys.stdin.readline().split('\n')[0].split(' ')
n,k=int(inputs[0]),int(inputs[1])
coins=[]
for i in range(n):
    coins.append(int(sys.stdin.readline()))

target=k
needCoins=0
for i in range(n-1,-1,-1):
    c=target//coins[i]
    if c>0:
        target-=coins[i]*c
        needCoins+=c

print(needCoins)
import sys

n=int(sys.stdin.readline())

tips=[]
for i in range(n):
    tips.append(int(sys.stdin.readline()))

tips.sort(reverse=True)

maxTip=0
for i in range(n):
    tip=tips[i]-i
    if tip<0:
        continue
    else:
        maxTip+=tip

print(maxTip)
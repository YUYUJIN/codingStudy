import sys

n=int(int(sys.stdin.readline()))
nums=[0 for _ in range(8001)]

for _ in range(n):
    nums[int(sys.stdin.readline())-4001]+=1

result=[]
sum=0
maxF=max(nums)
candidate=[]
numRange=False
minP,maxP=0,0
for i in range(len(nums)):
    sum+=(i-4000)*(nums[i])
    if nums[i]==maxF:
        candidate.append(i)
    if numRange:
        if nums[i]>0:
            maxP=i
    else:
        if nums[i]>0:
            numRange=True
            minP=i
result.append(round(sum/n))

temp=0
for i in range(len(nums)):
    temp+=nums[i]
    if temp>(n/2):
        break
result.append(i-4000)
    
if len(candidate)==1:
    result.append(candidate[0]-4000)
else:
    result.append(candidate[1]-4000)

if maxP==0:
    maxP=minP
result.append(maxP-minP)

for i in range(4):
    print(result[i])
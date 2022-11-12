import sys

s=sys.stdin.readline()
nums=[0]*10

for c in s:
    if c!='\n':
        nums[int(c)]+=1

for i in range(9,-1,-1):
    for j in range(nums[i]):
        print(i,end='')
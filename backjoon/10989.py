import sys

n=int(int(sys.stdin.readline()))         #빠른 입출력을 위해
nums=[0 for _ in range(10000)]

for _ in range(n):
    nums[int(sys.stdin.readline())-1]+=1

for i in range(10000):
    for j in range(nums[i]):
        print(i)
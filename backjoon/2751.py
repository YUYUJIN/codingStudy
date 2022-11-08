import random
import sys

#퀵정렬은 평균 O(nlogn) 최악 O(n^2)-> 역순일 때?
def quick_sort(nums):
    if len(nums)<=1:
        return nums
    p=nums[len(nums)//2]                       #그냥 pivot를 잡으면 시간초과
    #p=nums[random.randrange(0,len(nums)-1)]   #최선은 아니더라도 랜덤값으로
    low,equal,high=[],[],[]
    for num in nums:
        if num>p:
            high.append(num)
        elif num<p:
            low.append(num)
        else:
            equal.append(num)
    
    return quick_sort(low)+equal+quick_sort(high)

n=int(int(sys.stdin.readline()))         #빠른 입출력을 위해
nums=[]

for i in range(n):
    nums.append(int(int(sys.stdin.readline())))

random.shuffle(nums)    #최악을 피하기 위해 셔플     
nums=quick_sort(nums)

for i in range(n):
    print(nums[i])
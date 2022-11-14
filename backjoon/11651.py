import sys
import random

#파이썬 재귀호출 깊이 제한 변경
sys.setrecursionlimit(2500)

#퀵정렬은 평균 O(nlogn) 최악 O(n^2)-> 역순일 때?
def quick_sort(nums):
    if len(nums)<=1:
        return nums
    #그냥 pivot를 잡으면 시간초과
    px=nums[len(nums)//2][0]                   #후기 기준:x좌표
    py=nums[len(nums)//2][1]                   #초기 기준:y좌표
    #p=nums[random.randrange(0,len(nums)-1)]   #최선은 아니더라도 랜덤값으로
    low,high,equal=[],[],[]
    for num in nums:
        if num[1]>py:
            high.append(num)
        elif num[1]<py:
            low.append(num)
        else:                    #x좌표 동일
            if num[0]>px:
                high.append(num)
            elif num[0]<px:
                low.append(num)
            else:
                equal.append(num) #자기 자신
    
    return quick_sort(low)+equal+quick_sort(high)


n=int(sys.stdin.readline())

nums=[]

for i in range(n):
    coordinate=sys.stdin.readline().split('\n')[0].split(' ')
    nums.append([int(coordinate[0]),int(coordinate[1])])

random.shuffle(nums)    #최악을 피하기 위해 셔플     
nums=quick_sort(nums)

for i in range(n):
    print('{} {}'.format(nums[i][0],nums[i][1]))
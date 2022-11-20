def solution(numbers):
    answer = ''
    nums=[]
    for i in numbers:
        num=str(i)
        numOrd=num*3
        nums.append([num,numOrd])
    nums=sorted(nums,key=lambda x: x[1])       
    
    for i in range(len(nums)-1,-1,-1):
        answer+=nums[i][0]
    answer=str(int(answer))
    return answer
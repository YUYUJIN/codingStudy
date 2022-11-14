def solution(array):
    answer = 0
    nums=''
    for a in array:
        nums+=str(a)
    
    for n in nums:
        if n=='7':
            answer+=1
    return answer
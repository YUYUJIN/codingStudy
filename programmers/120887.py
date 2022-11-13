def solution(i, j, k):
    answer = 0
    nums=''
    strK=str(k)
    for n in range(i,j+1):
        nums+=str(n)
    for n in nums:
        if n==strK:
            answer+=1
    return answer
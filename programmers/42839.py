import math

def checkPrimN(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if (n%i)==0:
            return False
    return True

#순열
def P(result,num,depth,n,k):
    if depth==k:
        result.add(int(''.join(c for c in num[:k])))
        
    for i in range(depth,n):
        num[depth],num[i]=num[i],num[depth] #swap
        P(result,num,depth+1,n,k)
        num[depth],num[i]=num[i],num[depth] #swap
        
def solution(numbers):
    answer = 0
    
    list=[c for c in numbers]
    nums=set()
    for i in range(1,len(numbers)+1):
        P(nums,list,0,len(numbers),i)
    
    for n in nums:
        if checkPrimN(int(n)):
            answer+=1
        
    return answer
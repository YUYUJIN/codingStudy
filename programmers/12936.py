import math

def method(n,k,do,result):
    if n==1:
        result.append(do[0])
        return result
    else:
        t=(k-1)//math.factorial(n-1)
        result.append(do[t])
        del do[t]
        
        k=k%math.factorial(n-1)
        return method(n-1,k,do,result)
        
        
def solution(n, k):
    answer = []
    do=[i+1 for i in range(n)]
        
    answer=method(n,k,do,[])
    
    return answer
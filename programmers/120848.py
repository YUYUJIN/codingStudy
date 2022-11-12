def findMinFactorial(before,n,max):
    f=before*n
    if f==max:
        return n
    elif f>max:
        return n-1
    else:
        return findMinFactorial(f,n+1,max)

def solution(n):
    answer = findMinFactorial(1,1,n)
    return answer
def minFuel(n):
    if n<2:
        return n
    elif n%2==1:
        return minFuel(n//2)+1
    else:
        return minFuel(n//2)
    
def solution(n):
    ans = minFuel(n)

    return ans
#유클리드 호제법으로 최대공약수 구현
#gcd(a,b)=gcd(b,r) r-> a를 b로 나눈 나머지
def gcd(a,b):
    if b==0:
        return a
    else:
    	return gcd(b, a%b)
    
#lcm(a,b)*gcm(a,b)=a*b
def lcm(a,b):
    return (a*b)//gcd(a,b)

def solution(arr):
    answer = 0
    while len(arr)>1:
        n1=arr.pop()
        n2=arr.pop()
        arr.append(lcm(n1,n2))
    answer=arr[0]
    return answer
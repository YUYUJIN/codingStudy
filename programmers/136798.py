import math

def weaponSize(num):
    size=0
    for i in range(1,int(math.sqrt(num)+1)):
        if num%i==0:
            size+=1
    size*=2
    if num%(num**(1/2))==0:
        size-=1
    return size

def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        size=weaponSize(i)
        if size>limit:
            answer+=power
        else:
            answer+=size
    return answer
def nextpm(pm):
    result=pm
    for i,p in enumerate(pm):
        if p==1:
            result[i]=-1
            break
        else:
            result[i]=1
    return result

def solution(numbers, target):
    answer = 0
    pm=[1 for i in numbers]
    
    cases=2**(len(numbers))-1
    
    for c in range(cases):
        sums=0
        for i,n in enumerate(numbers):
            sums+=(n*pm[i])
        if sums==target:
            answer+=1
        pm=nextpm(pm)
        
    return answer
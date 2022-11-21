def solution(n, times):
    answer = 0
    times.sort()
    min=times[0]
    max=times[0]*n
    while min<=max:
        mid=min+(max-min)//2
        check=0
        for t in times:
            check+=mid//t
        if check<n:
            min=mid+1
        else:
            max=mid-1
    answer=min
    return answer

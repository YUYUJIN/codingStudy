def solution(sizes):
    answer = 0
    maxsize=[0,0]
    for size in sizes:
        size.sort()
        if maxsize[0]<size[0]:
            maxsize[0]=size[0]
        if maxsize[1]<size[1]:
            maxsize[1]=size[1]
    answer=maxsize[0]*maxsize[1]
    return answer
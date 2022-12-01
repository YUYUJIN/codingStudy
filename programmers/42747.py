def solution(citations):
    answer = 0
    citations.sort()
    maxNum=citations[-1]
    if maxNum>=1000:
        maxNum=1000
    i=0
    for candidate in range(1,maxNum+1):
        if i<len(citations):
            while citations[i]<candidate:
                i+=1
                if i>=len(citations):
                    i-=1
                    break
        h=len(citations)-i
        if candidate<=h and i<=candidate:
            answer=candidate
    return answer
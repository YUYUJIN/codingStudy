def solution(clothes):
    answer = 1
    category=dict()
    for c in clothes:
        if category.get(c[1]):
            category[c[1]]+=1
        else:
            category[c[1]]=1
    for c in category.keys():
        answer*=(category[c]+1)
    return answer-1
def oneChange(word,count,words,visited,end):
    do=[]
    
    for w in words:
        if w in visited:
            continue
        
        check=0
        for i in range(len(word)):
            if word[i]==w[i]:
                check+=1
        if check==(len(word)-1):
            do.append(w)
    
    while len(do)>0:
        tar=do.pop()
        if tar==end:
            return count+1
        visited.append(tar)
        return oneChange(tar,count+1,words,visited,end)

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return answer
    else:
        return oneChange(begin,0,words,[],target)
    return answer
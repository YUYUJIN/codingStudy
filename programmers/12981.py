def solution(n, words):
    back=words[0][-1]
    spokenword=[words[0]]
    for i in range(1,len(words)):
        isEnd=False
        if back!=words[i][0]:
            isEnd=True
        elif words[i] in spokenword:
            isEnd=True
        
        if isEnd:
            return [i%n+1,i//n+1]
        else:
            spokenword.append(words[i])
            back=words[i][-1]
    return [0,0]
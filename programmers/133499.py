import re

words=['ye','ma','aya','woo']

def checkWords(s):
    wordCount=0
    for i in range(len(words)):
        if i<2:
            wordCount+=len(re.findall(words[i],s))*2
            wordCount-=len(re.findall(words[i]+words[i],s))*2
        else:  
            wordCount+=len(re.findall(words[i],s))*3
            wordCount-=len(re.findall(words[i]+words[i],s))*3
    if wordCount==len(s):
        return True
    else:
        return False
def solution(babbling):
    answer = 0
    for word in babbling:
        if checkWords(word):
            answer+=1
    return answer
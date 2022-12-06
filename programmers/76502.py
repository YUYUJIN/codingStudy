def shiftPH(s):
    result=''
    for i,c in enumerate(s):
        if i==0:
            continue
        result+=c
    result+=s[0]
    return result

def checkPH(s):
    stack=[]
    for c in s:
        if c=='(' or c=='[' or c=='{':
            stack.append(c)
        elif len(stack)>0:
            last=stack.pop(-1)
            if last=='(' and c==')':
                continue
            elif last=='[' and c==']':
                continue
            elif last=='{' and c=='}':
                continue
            else:
                return False
        else:
            return False
    if len(stack)==0:
        return True
    else:
        return False

def solution(s):
    answer = 0
    for i in range(len(s)):
        if checkPH(s):
            answer+=1
        s=shiftPH(s)
    return answer
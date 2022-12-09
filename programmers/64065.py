def makeSetList(s):
    result=[]
    temp=''
    setOpen=False
    for c in s[1:len(s)-1]:
        if c=='{':
            setOpen=True
            inerSet=set()
        elif c=='}':
            setOpen=False
            inerSet.add(int(temp))
            temp=''
            
            result.append(inerSet)
        elif ord(c)>=ord('0') and ord(c)<=ord('9'):
            temp+=c
        elif c==',' and setOpen:
            inerSet.add(int(temp))
            temp=''
    return result
def makeList(setList):
    result=[]
    resultSet=set()
    for sets in setList:
        num=list(sets-resultSet)[0]
        result.append(num)
        resultSet.add(num)   
    return result
def solution(s):
    answer = []
    setList=makeSetList(s)
    setList=sorted(setList,key=lambda x:len(x))
    answer=makeList(setList)
    return answer
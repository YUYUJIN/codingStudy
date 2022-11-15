def solution(number, k):
    answer = ''
    remainK=k
    remove=False
    for i in range(len(number)):
        remove=False
        backword=i+1+remainK
        if backword>=len(number):
            backword=len(number)
        for j in range(i+1,backword):
            if number[i]=='9' and backword>=remainK:
                break
            if int(number[i])<int(number[j]):
                remove=True
                remainK-=1
                break
        if remainK<=0:
                break
        if remove:
            continue
        else:
            answer+=number[i]
            
    if i==len(number)-1:
        answer=number[:len(number)-remainK]
    else:
        answer+=number[i+1:]
    return answer
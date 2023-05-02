man1=[1,2,3,4,5]
man2=[2,1,2,3,2,4,2,5]
man3=[3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    answer = []
    score=[0,0,0]
    for i in range(len(answers)):
        if answers[i]==man1[i%5]:
            score[0]+=1
        if answers[i]==man2[i%8]:
            score[1]+=1
        if answers[i]==man3[i%10]:
            score[2]+=1
    maxs=0
    for s in score:
        if maxs<=s:
            maxs=s
    for i in range(len(score)):
        if score[i]==maxs:
            answer.append(i+1)
    return answer
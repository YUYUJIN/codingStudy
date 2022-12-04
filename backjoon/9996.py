import sys

class checker:
    def __init__(self,s):
        self.forword=''
        self.backword=''
        isforword=True
        for c in s:
            if ord(c)==42:
                isforword=False
                continue
            if isforword:
                self.forword+=c
            else:
                self.backword=c+self.backword
    def check(self,s):
        if len(s)<len(self.forword)+len(self.backword):
            return 'NE'
        for i in range(len(s)):
            if i<len(self.forword):
                if s[i]!=self.forword[i]:
                    return 'NE'
            if i<len(self.backword):
                if s[-(i+1)]!=self.backword[i]:
                    return 'NE'
        return 'DA'

n=int(sys.stdin.readline())
s_in=sys.stdin.readline().split('\n')[0]
che=checker(s_in)

answer=[]
for i in range(n):
    s=sys.stdin.readline().split('\n')[0]
    answer.append(che.check(s))

for i in range(n):
    print(answer[i])

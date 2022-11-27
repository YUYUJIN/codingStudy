import sys

def recursion(s, l, r,recur):
    recur+=1
    if l >= r: return 1,recur
    elif s[l] != s[r]: return 0,recur
    else: return recursion(s, l+1, r-1,recur)

def isPalindrome(s):
    recur=0
    result,recur=recursion(s, 0, len(s)-1,recur)
    return recur,result

t=int(sys.stdin.readline())
answer=[]
for i in range(t):
    s=sys.stdin.readline().split('\n')[0]
    result,recur=isPalindrome(s)
    answer.append([result,recur])

for i in range(t):
    print(answer[i][1],answer[i][0])



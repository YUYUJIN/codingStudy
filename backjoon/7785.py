import sys

n=int(sys.stdin.readline())
M={}

for i in range(n):
    s=sys.stdin.readline().split('\n')[0].split(' ')
    name,state=s[0],s[1]
    if state == 'enter':
        M[name]=True
    else:
        del M[name]

answer=list(M.keys())
answer.sort(reverse=True)
for a in answer:
    print(a)

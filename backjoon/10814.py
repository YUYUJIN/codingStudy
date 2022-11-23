import sys

n=int(sys.stdin.readline())
#members=[[]]*200  파이썬 주소 방식 특성 상 같은 주소를 가르키게됨
members=[[] for i in range(200)]

for i in range(n):
    s=sys.stdin.readline().split('\n')[0].split(' ')
    age,name=int(s[0]),s[1]
    members[age-1].append(name)
    
for i in range(200):
    for j in range(len(members[i])):
        print(i+1,members[i][j])
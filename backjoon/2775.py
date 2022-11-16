import sys

def countPeoples(k,n):
    house=[[i+1 for i in range(n)]]
    for i in range(k):
        peoples=[house[i][0]]
        for j in range(1,n):
            peoples.append(peoples[j-1]+house[i][j])
        house.append(peoples)
    return house[k][n-1]

T=int(sys.stdin.readline())

peoples=[]
for i in range(T):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    peoples.append(countPeoples(k,n))

for i in range(T):
    print(peoples[i])



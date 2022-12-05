import sys

def check8x8(board88):
    case1='WBWBWBWB'
    case2='BWBWBWBW'
    case1count=0
    case2count=0
    reverse=False
    for line in board88:
        if reverse:
            for i in range(len(line)):
                if line[i]!=case1[i]:
                    case2count+=1
                if line[i]!=case2[i]:
                    case1count+=1
        else:
            for i in range(len(line)):
                if line[i]!=case1[i]:
                    case1count+=1
                if line[i]!=case2[i]:
                    case2count+=1
        reverse=not(reverse)
        
    return min(case1count,case2count)

def checkBoard(board,m,n):
    minCount=64 # 최대 경우의 수
    for i in range(m-7):
        for j in range(n-7):
            board88=[]
            for k in range(i,i+8):
                board88.append(board[k][j:j+8])
            count=check8x8(board88)
            if count<minCount:
                minCount=count
    return minCount
            

m,n=map(int,sys.stdin.readline().split('\n')[0].split())

board=[]
for i in range(m):
    board.append(sys.stdin.readline().split('\n')[0])

print(checkBoard(board,m,n))
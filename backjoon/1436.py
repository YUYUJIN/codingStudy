import sys

def check666(num):
    number=str(num)
    for i in range(len(number)-2):
        if number[i]=='6' and number[i+1]=='6' and number[i+2]=='6':
            return True
    return False 

n=int(sys.stdin.readline())

target=666
count=0
while True:
    if check666(target):
        count+=1
    
    if count==n:
        print(target)
        break
    target+=1

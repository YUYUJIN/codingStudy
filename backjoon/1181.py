import sys

n=int(sys.stdin.readline())

words=[]

for i in range(n):
    word=sys.stdin.readline().split('\n')[0]
    words.append(word)

words=list(set(words))
words=sorted(words,key=lambda x:(len(x),x))

for word in words:
    print(word)
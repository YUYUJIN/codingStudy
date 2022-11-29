import math

class node:
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None
class tournment:
    def __init__(self,size):
        self.root=node()
        self.height=int(math.log2(size))
        self.size=size
    #한명이 우승하는 토너먼트 트리를 만듬
    def makeTree(self,winner):
        n=self.size//2
        current=self.root
        current.data=winner
        for i in range(self.height):
            if n>=winner:
                current.left=node()
                current=current.left
                current.data=winner
                n-=math.pow(2,self.height-i-2)
            else:
                current.right=node()
                current=current.right
                current.data=winner
                n+=math.pow(2,self.height-i-2)
    #상대를 맞날 때까지 탐색
    def findMeet(self,opponent):
        n=self.size//2
        current=self.root
        meetPos=0 #root 기준
        for i in range(self.height):
            if n>=opponent:
                if current.left is None:
                    break
                current=current.left
                n-=math.pow(2,self.height-i-2)
            else:
                if current.right is None:
                    break
                current=current.right
                n+=math.pow(2,self.height-i-2)
        meetPos=i
        return self.height-meetPos

def solution(n,a,b):
    t=tournment(n)
    t.makeTree(a)
    return t.findMeet(b)
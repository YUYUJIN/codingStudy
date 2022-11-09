class node():
    def __init__(self):
        self.data=None
        self.left=None
        self.right=None    
class morseTree():
    def __init__(self):
        self.root=node()
    def makeTree(self,morse):
        for i in range(len(morse)):
            currentNode=self.root
            for c in morse[i]:
                if c=='.':
                    if currentNode.left==None:
                        currentNode.left=node()
                    currentNode=currentNode.left
                else:
                    if currentNode.right==None:
                        currentNode.right=node()
                    currentNode=currentNode.right
            currentNode.data=chr(97+i)             #아스키코드 97:a
    def decoding(self,letter):
        result=''
        currentNode=self.root
        for c in letter:
            if c=='.':
                currentNode=currentNode.left
            elif c=='-':
                currentNode=currentNode.right
            else:
                result+=currentNode.data
                currentNode=self.root         #단어 종료시마다 다시 탐색을 위해 루트노드로 이동
        result+=currentNode.data              #letter 마지막은 그냥 종료되기에 최종값 더하기
        return result
            
morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
def solution(letter):
    answer=''
    MT=morseTree()
    MT.makeTree(morse)
    answer=MT.decoding(letter)
    return answer
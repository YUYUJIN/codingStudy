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
            currentNode.data=chr(97+i)
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
                currentNode=self.root
        result+=currentNode.data
        return result
            
morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
def solution(letter):
    answer=''
    MT=morseTree()
    MT.makeTree(morse)
    answer=MT.decoding(letter)
    return answer
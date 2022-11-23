import math

def solve(brown,yellow):
    #y=(brown+yellow)/x
    #ax^2+bx+c=2x^2+(4+brown)x-2(brown+yellow)
    a=2
    b=(-1)*(4+brown)
    c=2*(brown+yellow)
    x1=(-b+math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
    x2=(-b-math.sqrt(math.pow(b,2)-(4*a*c)))/(2*a)
    y1=(brown+yellow)/x1
    y2=(brown+yellow)/x2
    return (x1,y1),(x2,y2)
def solution(brown, yellow):
    #연립방정식 허근은 존재하지 않음
    #(x-2)(y-2)=yellow
    #xy-yellow=brown
    answer1,answer2=solve(brown,yellow)
    if answer1[0]>=answer1[1]:
        return answer1
    else:
        return answer2
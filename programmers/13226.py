def solution(topping):
    answer=0
    mans1=set()
    otherToppings={}
    for i in topping:
        try:
            otherToppings[str(i)]+=1
        except:
            otherToppings[str(i)]=1
    for i in topping:
        mans1.add(i)
        if otherToppings[str(i)]>1:
            otherToppings[str(i)]-=1
        else:
            del otherToppings[str(i)]
        if len(mans1)==len(otherToppings):
            answer+=1
    return answer
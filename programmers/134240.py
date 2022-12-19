def solution(food):
    answer = ''
    for i in range(1,len(food)):
        foodCount=food[i]//2
        for j in range(foodCount):
            answer+=str(i)
    answer+='0'
    answer+=answer[-2::-1]
        
    return answer
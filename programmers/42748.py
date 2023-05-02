def solution(array, commands):
    answer = []
    for c in commands:
        target=array[c[0]-1:c[1]]
        target.sort()
        answer.append(target[c[2]-1])
    return answer
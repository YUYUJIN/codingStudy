def solution(arr1, arr2):
    answer = []
    for col1 in arr1:
        row=[]
        for i in range(len(arr2[0])):
            sum=0
            for j in range(len(col1)):
                sum+=col1[j]*arr2[j][i]
            row.append(sum)
        answer.append(row)
            
    return answer
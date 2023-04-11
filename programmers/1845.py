def solution(nums):
    answer = 0
    ponketmons=dict()
    for n in nums:
        ponketmons[n]=1
    answer=min(len(ponketmons.keys()),int(len(nums)/2))
    return answer
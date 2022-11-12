def solution(before, after):
    beforeF=[0]*26
    afterF=[0]*26
    for c in before:
        beforeF[ord(c)-97]+=1      #'a'->97
    for c in after:
        afterF[ord(c)-97]+=1
    if beforeF==afterF:
        return 1
    else:
        return 0
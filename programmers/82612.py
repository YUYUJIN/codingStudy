def solution(price, money, count):
    answer = -1
    price_sum=0
    for c in range(count):
        price_sum+=(price*(c+1))
    answer=money-price_sum
    if answer>=0:
        answer=0
    else:
        answer=-answer
    return answer
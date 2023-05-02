def solution(phone_book):
    answer = True
    numbers=dict()
    phone_book.sort(key=lambda x:len(x))
    for pb in phone_book:
        for n in range(len(pb)):
            if numbers.get(pb[:n]):
                answer=False
        numbers[pb]=1
    return answer
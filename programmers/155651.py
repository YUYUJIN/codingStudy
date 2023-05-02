def solution(book_time):
    answer = 0
    book_minute=[]
    for b in book_time:
        start=b[0].split(':')
        end=b[1].split(':')
        book_minute.append([int(start[0])*60+int(start[1]),'start'])
        book_minute.append([int(end[0])*60+int(end[1])+10,'end'])
    book_minute.sort()
    
    room=0
    for b in book_minute:
        if b[1]=='start':
            room+=1
        else:
            room-=1
        answer=max(answer,room)
    return answer
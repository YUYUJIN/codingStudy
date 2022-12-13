import sys
import heapq

n=int(sys.stdin.readline())

schedule=[]
meetingRoom=[]
for i in range(n):
    schedule.append(tuple(map(int,sys.stdin.readline().split('\n')[0].split())))

schedule=sorted(schedule,key=lambda x:x[0])

for i in range(n):
    if len(meetingRoom)<1:
        heapq.heappush(meetingRoom,schedule[i][1])
    else:
        if meetingRoom[0]<=schedule[i][0]:
            heapq.heappop(meetingRoom)
        heapq.heappush(meetingRoom,schedule[i][1])

print(len(meetingRoom))
    

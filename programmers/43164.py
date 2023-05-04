import copy

def airLine(start,route,ticket_dict,doneCount):
    if not ticket_dict.get(start):
        back=copy.deepcopy(route)
        back.append(start)
        return back
    pre=copy.deepcopy(route)
    pre.append(start)
    tkd=copy.deepcopy(ticket_dict)
    coor=tkd[start]
    for i in range(len(coor)):
        tkd[start]=coor[:i]+coor[i+1:]
        back=airLine(coor[i],pre,tkd,doneCount)
        if len(back)==doneCount:
            return back
    return route
        
def solution(tickets):
    ticket_dict=dict()
    start='ICN'
    
    for t in tickets:
        if ticket_dict.get(t[0]):
            ticket_dict[t[0]].append(t[1])
        else:
            ticket_dict[t[0]]=[t[1]]
    
    for key in ticket_dict.keys():
        ticket_dict[key].sort()
    return airLine(start,[],ticket_dict,len(tickets)+1)
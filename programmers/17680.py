def solution(cacheSize, cities):
    cache=[]
    runtime=0
    for i in range(len(cities)):
        cacheHit=False
        city=cities[i].lower()
        
        for j in range(len(cache)):
            if city==cache[j]:
                cache.pop(j)
                cacheHit=True
                break
                
        if cacheHit:
            runtime+=1
        else:
            runtime+=5
        
        cache.append(city)
        if len(cache)>cacheSize:
            cache.pop(0)
    
    return runtime

print(solution(3,["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
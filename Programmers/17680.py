from collections import deque
def solution(cacheSize, cities):
    if cacheSize==0:
        return len(cities)*5
    answer = 0
    cache=deque([])
    for i in cities:
        #대소문자 구분 X
        i=i.lower()
        
        #hit!
        if i in cache:
            cache.remove(i)
            cache.appendleft(i)
            answer+=1
        #miss 중 cache가 남을 때
        elif len(cache) < cacheSize:
            cache.appendleft(i)
            answer+=5
        #miss 지만 cache가 차있을 때
        else:
            cache.pop()
            cache.appendleft(i)
            answer+=5
    return answer

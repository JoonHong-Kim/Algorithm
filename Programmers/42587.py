from collections import deque
def solution(priorities, location):
    answer=0
    #(우선순위,index) 큐
    deq=deque([(v,index) for index,v in enumerate(priorities)])
    while deq:
        tmp=deq.popleft()

        if deq and max(deq)[0] > tmp[0]:
            deq.append(tmp) 
        else:
            answer+=1
            if tmp[1]==location:
                break
    return answer

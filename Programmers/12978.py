from collections import defaultdict
import heapq
import sys

def solution(N, road, K):
    answer = 0
    graph=defaultdict(dict)
    for i in road:
        if graph[i[0]].get(i[1]) and graph[i[0]][i[1]] < i[2]:
            continue
        graph[i[0]][i[1]]=i[2]
        graph[i[1]][i[0]]=i[2]
    
    #거리 최대 10000
    distance={i:sys.maxsize for i in range(1,N+1)}
    #1 기준 거리
    distance[1]=0
    queue=[]
    #스타트 1로
    heapq.heappush(queue,[0,1])
    
    #다익스트라
    while queue:
        c_dist,c_dest=heapq.heappop(queue)
        #기존 거리보다 길면 스킵
        if distance[c_dest] < c_dist:
            continue
        #그래프에서 뽑아서 갱신
        for n_dest,n_dist in graph[c_dest].items():
            dist=c_dist+n_dist
            if distance[n_dest] > dist:
                distance[n_dest]=dist
                heapq.heappush(queue,[dist,n_dest])
    #K이하 갯수 카운트
    for i in distance.items():
        if i[1] <= K:
            answer+=1
    return answer

from collections import defaultdict
import heapq
INF = 1e9
def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    set_summit = set(summits)
    for path in paths:
        graph[path[0]].append((path[1], path[2]))
        graph[path[1]].append((path[0], path[2]))
    def dijkstra():
        q = []
        intensity = [INF for _ in range(n+1)]
        # 출입구 모두 0으로
        for gate in gates:
            intensity[gate] = 0
            heapq.heappush(q, (0, gate))
        while q:
            weight,node = heapq.heappop(q)

            if node in set_summit: #or weight > intensity[node]:
                continue
            
            for next_node,next_weight  in graph[node]:
                new_weight = max(weight, next_weight)
                if new_weight < intensity[next_node]:
                    intensity[next_node] = new_weight
                    heapq.heappush(q, (new_weight,next_node))
        return intensity
    intensity = dijkstra()
    summits.sort(key = lambda x: (intensity[x],x))
    return [summits[0], intensity[summits[0]]]
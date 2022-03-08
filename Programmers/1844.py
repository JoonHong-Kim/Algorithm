from collections import deque 

def solution(maps):
    n=len(maps)
    m=len(maps[0])
    #방문 확인겸 거리 저장용
    visited=[[0 for _ in range(m)] for _ in range(n)]
    #움직임 저장용
    dx,dy=[1,-1,0,0],[0,0,1,-1]
    #0,0 부터 시작
    queue=deque([[0,0]])
    #첫 블록 = 1 
    visited[0][0]=1
    
    #갈 공간이 없을 때까지
    while queue:
        x,y=queue.popleft()
        
        #좌우 위아래
        for i in range(4):
            n_x=x+dx[i]
            n_y=y+dy[i]
            
            #list 범위 안벗어나게
            if 0<=n_x<m and 0<=n_y<n:
                #방문 한적이 없고 벽이 아닐 때
                if not visited[n_y][n_x] and maps[n_y][n_x]:
                    #전 블록 +1
                    visited[n_y][n_x]=visited[y][x]+1
                    #큐에 넣음
                    queue.append([n_x,n_y])
                    
    #방문 불가능 -> -1 return
    return visited[-1][-1] if visited[-1][-1] else -1

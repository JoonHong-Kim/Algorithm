from collections import deque

def solution(rows, columns, queries):
    answer=[]
    # row x columns 배열 만들기
    rot = [[i*columns+j+1 for j in range(columns)] for i in range(rows)]
    
    for query in queries:
        tmp=deque([])
        
        #회전+최솟값 찾기위에 데크에 범위 저장
        for i in range(query[1]-1,query[3]-1):
            tmp.append(rot[query[0]-1][i])
        for i in range(query[0]-1,query[2]-1):
            tmp.append(rot[i][query[3]-1])
        for i in reversed(range(query[1],query[3])):
            tmp.append(rot[query[2]-1][i])
        for i in reversed(range(query[0],query[2])):
            tmp.append(rot[i][query[1]-1])
        answer.append(min(tmp))
        tmp.rotate(1)
        
        #돌린거 다시 넣기
        pointer=0
        for i in range(query[1]-1,query[3]-1):
            rot[query[0]-1][i]=tmp[pointer]
            pointer+=1
        for i in range(query[0]-1,query[2]-1):
            rot[i][query[3]-1]=tmp[pointer]
            pointer+=1
        for i in reversed(range(query[1],query[3])):
            rot[query[2]-1][i]=tmp[pointer]
            pointer+=1
        for i in reversed(range(query[0],query[2])):
            rot[i][query[1]-1]=tmp[pointer]
            pointer+=1
            
    return answer

from itertools import chain

def solution(n):
	#1,2,3,4...n 개로 늘어감
    snail=[[0 for _ in range(i+1)] for i in range(n)]
    #처음 위에서 아래니까 y=-1
    x,y=0,-1
    #입력할 숫자
    num=1
    #방향 n번
    for direct in range(n):
        for tri in range(direct,n):
        	#아래
            if direct%3==0:
                y+=1
            #오른쪽
            elif direct %3 ==1:
                x+=1
            #위
            else:
                x-=1
                y-=1
            snail[y][x]=num
            num+=1
    #배열 붙이기
    return list(chain(*snail))

from itertools import combinations as combi

def solution(relation):
    col=range(len(relation[0]))
    row_len=len(relation)
    #모든 경우의수
    candi=[]
    for i in range(1,len(col)+1):
        candi.extend(combi(col,i))
    #유일성
    uniques=[]
    for i in candi:
        tmp=set([tuple(x[j] for j in i) for x in relation])
        if len(tmp)==row_len:
            uniques.append(set(i))
    #삭제 오류 방지
    answer=uniques[:]
    # 최소성 
    for index,value in enumerate(uniques):
        for j in uniques[index+1:]:
            if value==value&j and (j in answer):
                answer.remove(j)
    return len(answer)

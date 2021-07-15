from itertools import combinations

def solution(orders, course):
    answer = []
    dic={}
    spl_ord=[set(list(i)) for i in orders]
    for i,v in enumerate(spl_ord):
        if i+1 ==len(spl_ord):
            break
        for j in spl_ord[i+1:]:
            tmp=(v&j)
            tmp=sorted(list(tmp))
            for k in course:
                x=list(combinations(tmp,k))
                for re in x:
                    re=''.join(list(re))
                    if re in dic:
                        dic[re]+=1
                    else:
                        dic[re]=1
    for c in course :
        arr = []
        maxNum = 0
        for key, value in dic.items() :
            if len(key) == c :
                if maxNum < value :
                    arr = [key]
                    maxNum = value
                elif maxNum == value :
                    arr.append(key)
        for i in range(len(arr)):
            answer.append(arr[i])
    return sorted(answer)

from itertools import permutations
def is_prime(n):
    if n==1 or n==0:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
def solution(numbers):
    x=[]
    
    #경우의 수 1개~ n개 붙일때
    for i in range(1,len(numbers)+1):
        x.extend(list(permutations(numbers,i)))
    #숫자로 변경
    y=[int(''.join(i)) for i in x]
    #중복제거
    y=set(y)
    answer=0
    for i in y:
        if is_prime(i):
            answer+=1
    return answer

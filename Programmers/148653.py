#https://school.programmers.co.kr/learn/courses/30/lessons/148653
def solution(storey):
    answer = 0
    while storey != 0:
        last = storey % 10
        if last > 5 or (last == 5 and storey // 10 % 10 >= 5):
            answer += 10 - last
            storey += 10 - last
        else:
            answer += last
        storey //= 10
    return answer
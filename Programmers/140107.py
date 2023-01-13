# https://school.programmers.co.kr/learn/courses/30/lessons/140107
import math


def solution(k, d):
    max_y = [int(math.sqrt(d**2 - i**2)) for i in range(0, d + 1, k)]
    count = [i // k + 1 for i in max_y]
    return sum(count)

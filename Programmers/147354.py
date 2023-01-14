# https://school.programmers.co.kr/learn/courses/30/lessons/147354
from functools import reduce


def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    hashs = []
    for i in range(row_begin, row_end + 1):
        s_i = sum([j % (i - 1) for j in data[i]])
        hashs.append(s_i)
    answer = reduce(lambda x, y: x ^ y, hashs)
    return answer

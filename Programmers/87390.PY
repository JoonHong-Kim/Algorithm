def solution(n, left, right):
    left_y = left // n
    right_y = right // n
    left_x = left % n
    right_x = right % n
    answer = []
    for y in range(left_y, right_y + 1):
        for x in range(1, n + 1):
            answer.append(max(x, y+1))
    if right_x == n - 1:
        answer = answer[left_x:]
    else:
        answer = answer[left_x:-(n-right_x)+1]
    return answer
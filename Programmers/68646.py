def solution(a):
    answer = 0
    left = []
    right = []
    left_min = 10e10
    right_min = 10e10

    # left min 값들 list
    for i in a:
        if i < left_min:
            left_min = i
        left.append(left_min)

    # right min 값들 list
    for j in a[::-1]:
        if j < right_min:
            right_min = j
        right.append(right_min)
    right.reverse()

    for idx, k in enumerate(a):
        # 어차피 무조건 됨
        if idx == 0 or idx == len(a) - 1:
            answer += 1
            continue

        left_min = left[idx - 1]
        right_min = right[idx + 1]
        # 둘다 크면 안됨
        if left_min < k and right_min < k:
            continue

        answer += 1
    return answer

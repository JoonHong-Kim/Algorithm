import math


def solution(enroll, referral, seller, amount):
    person_map = {i: v for i, v in zip(enroll, referral)}
    result_map = {i: 0 for i in enroll}
    for s, a in zip(seller, amount):
        upper = a * 100
        ptr = s
        while True:
            result_map[ptr] += math.ceil(upper * 0.9)
            if upper < 10 or person_map[ptr] == "-":
                break

            upper = int(upper * 0.1)
            ptr = person_map[ptr]

    answer = [v for _, v in result_map.items()]
    return answer

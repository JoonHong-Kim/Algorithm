#https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product


def solution(users, emoticons):
    discounts = [10, 20, 30, 40]
    candidates = []
    for d in product(discounts, repeat=len(emoticons)):
        dis_emoticons = [x * (100 - y) / 100 for x, y in zip(emoticons, d)]
        emo_plus_count = 0
        total_spend = 0
        for user in users:
            user_spend = 0
            for idx, emoticon in enumerate(dis_emoticons):
                if d[idx] >= user[0]:
                    if user_spend + emoticon >= user[1]:
                        user_spend = 0
                        emo_plus_count += 1
                        break
                    else:
                        user_spend += emoticon
            total_spend += user_spend
        candidates.append([emo_plus_count, total_spend])
    candidates.sort(key=lambda x: (-x[0], -x[1]))
    return candidates[0]

from collections import Counter


def solution(str1, str2):
    # 대문자로 바꿔줌
    new_str1 = str1.upper()
    new_str2 = str2.upper()
    st1 = []
    st2 = []
    # 두개씩 묶어서 알파벳만 있으면 추가
    for x, y in zip(new_str1, new_str1[1:]):
        if (x + y).isalpha():
            st1.append(x + y)
    for x, y in zip(new_str2, new_str2[1:]):
        if (x + y).isalpha():
            st2.append(x + y)

    # 둘다 0이면 1 출력
    if not st1 and not st2:
        return 65536

    # Counter 사용해서 교집합
    ints = Counter(st1) & Counter(st2)
    ints = len(list(ints.elements()))
    unio = len(list(unio.elements())) - ints

    answer = int(ints / unio * 65536)
    return answer

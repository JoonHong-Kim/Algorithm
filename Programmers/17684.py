def solution(msg):
    index_dict = {chr(ord("A") + i): i + 1 for i in range(26)}
    if len(msg) == 1:
        return [index_dict[msg]]
    answer = []
    pointer = 0
    next_pointer = 1
    while next_pointer < len(msg):
        check = msg[pointer : next_pointer + 1]
        if check in index_dict:
            next_pointer += 1
        else:
            index_dict[check] = len(index_dict) + 1
            answer.append(index_dict[msg[pointer:next_pointer]])
            pointer = next_pointer
            next_pointer += 1
    answer.append(index_dict[msg[pointer:next_pointer]])
    return answer

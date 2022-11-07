def solution(queue1, queue2):
    answer = 0
    sum_1 = sum(queue1)
    total = sum_1 + sum(queue2)
    
    target = total / 2
    
    # if sum value is odd
    if target % 1 != 0:
        return -1
    
    queue_ = queue1 + queue2
    len_q = len(queue_)

    first_ptr = 0
    second_ptr = len(queue1)
    while first_ptr <= second_ptr and second_ptr < len_q:
        if sum_1 == target:
            return answer
        elif sum_1 > target:
            sum_1 -= queue_[first_ptr]
            first_ptr += 1
        else:
            sum_1 += queue_[second_ptr]
            second_ptr += 1
        answer +=1
    return -1
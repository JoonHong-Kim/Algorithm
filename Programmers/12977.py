from itertools import combinations
from typing import List


def solution(nums: List[int]) -> int:
    # 제한사한이 적으니 제일 편한걸로..
    def is_prime(num: int) -> bool:
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    answer = 0
    all_combi = list(combinations(nums, 3))
    for i in all_combi:
        if is_prime(sum(i)):
            answer += 1

    return answer


if __name__ == "__main__":
    assert (
        solution([1, 2, 3, 4]) == 1
    ), f"The solution result is {solution([1,2,3,4])} but it should be 1"
    assert (
        solution([1, 2, 7, 6, 4]) == 4
    ), f"The solution result is {solution([1,2,7,6,4])} but it should be 4"
    print("All tests passed")

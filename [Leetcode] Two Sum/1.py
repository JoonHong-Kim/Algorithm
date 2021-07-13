from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for idx,v in enumerate(nums):
            find_n=target-v
            if find_n in seen:
                return [seen[find_n],idx]
            seen[v]=idx

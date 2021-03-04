from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {v:i for i,v in enumerate (nums)}
        for i, num in enumerate(nums):
            num2 = target - num
            if num2 in d and d[num2] != i:
                j=d[num2]
                return [i, j]
                print(d)

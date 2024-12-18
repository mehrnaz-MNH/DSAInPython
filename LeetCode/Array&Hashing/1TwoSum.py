
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_set = {}
        for i , num  in enumerate(nums):
            diff = target - num
            if diff in nums_set :
                return [ i  , nums_set[diff]]
            else :
                nums_set[num] = i



# time complexity in leetcode : 0ms 

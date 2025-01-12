from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mi = lo + (hi - lo) // 2
            if target == nums[mi]:
                return mi

            if nums[lo] <= nums[mi]:
                if nums[lo] <= target < nums[mi]:
                    hi = mi - 1
                else:
                    lo = mi + 1
            else:
                if nums[mi] < target <= nums[hi]:
                    lo = mi + 1
                else:
                    hi = mi - 1

        return -1
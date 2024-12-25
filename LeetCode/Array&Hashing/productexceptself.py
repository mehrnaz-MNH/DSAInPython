from typing import List


def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)

    suffix_arr = [1] * n
    for i in range(n - 2, -1, -1):
        suffix_arr[i] = suffix_arr[i + 1] * nums[i + 1]

    prefix_arr = [1] * n
    for i in range(1, n):
        prefix_arr[i] = prefix_arr[i - 1] * nums[i - 1]

    result_arr = [suffix_arr[i] * prefix_arr[i] for i in range(n)]

    return result_arr

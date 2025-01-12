from typing import List


def search(nums: List[int], t: int) -> int:

    l = 0
    r = len(nums) - 1

    while l <= r:
        m_i = l + (r-l) // 2
        if t > nums[m_i]:
            l = m_i + 1

        elif t < nums[m_i]:
            r = m_i - 1
        else:
            return m_i


    return -1


print(search([-1,0,3,5,9,12] , 9))


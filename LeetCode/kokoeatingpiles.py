from typing import List


class Solution:

    def checkIfValid(self, piles, m, h):
        time = 0
        for p in piles:
            time += p // m
            if p % m != 0:
                time += 1

        return time <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        hi = max(piles)
        res = hi
        while l <= hi:
            m = l + (hi - l) // 2
            if self.checkIfValid(piles, m, h):
                res = m
                hi = m - 1

            else:
                l = m + 1

        return res



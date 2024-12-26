from typing import List

# my solution , time complexity of O(k log n )
# def longestConsecutive(self, nums: List[int]) -> int:
#     if len(nums) == 0:
#         return 0
#
#     sorted_set = sorted(set(nums))
#     len_of_seq = 1
#     seqs = []
#
#     for i in range(len(sorted_set) - 1):
#         if sorted_set[i + 1] - sorted_set[i] == 1:
#             len_of_seq += 1
#         else:
#             seqs.append(len_of_seq)
#             len_of_seq = 1
#
#     seqs.append(len_of_seq)
#
#     return max(seqs)

# optimal solution , time complexity of O(n)
def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                after = num + 1
                while after in nums_set:
                    after += 1
                longest = max(longest, after - num)

        return longest


from typing import List


# hashing and bucket sort

def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq_dict = {}
    freq = [[] for i in range(len(nums) + 1)]

    for num in nums:
        freq_dict[num] = 1 + freq_dict.get(num, 0)
    for num, count in freq_dict.items():
        freq[count].append(num)
    print(freq)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for num in freq[i]:
            res.append(num)
            if len(res) == k:
                return res
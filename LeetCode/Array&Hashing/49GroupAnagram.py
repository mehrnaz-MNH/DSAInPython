from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_set = defaultdict(list)
        for str in strs :
            freq = [0]* 26
            for c in str :
                freq[ord(c) - ord('a')] +=1

            anag_set[tuple(freq)].append(str)


        return list(anag_set.values())

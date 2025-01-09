from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = list(zip(*strs))
        pref = ""
        for i in l:
            if len(set(i)) == 1:
                pref += i[0]
            else:
                break
        return pref
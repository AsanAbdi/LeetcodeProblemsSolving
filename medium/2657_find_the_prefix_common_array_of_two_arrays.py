from typing import List

class Solution:
    def findThePrefixCommonArray(self, a: List[int], b: List[int]) -> List[int]:
        c = []
        n = len(a)
        for i in range(1, 1+n):
            c.append(abs(len(set(a[:i] + b[:i])) - len(a[:i] + b[:i])))
        return c
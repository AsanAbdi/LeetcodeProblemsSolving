from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(int, list(str(int(''.join(list(map(str, digits))))+1))))
        return digits

        
from math import log

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return True if log(n, 3).is_integer() or 3 ** round(log(n, 3), 0) == n else False
        
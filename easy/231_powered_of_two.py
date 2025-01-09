from math import log
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return True if round(log(n,2), 10) == int(log(n, 2)) else False
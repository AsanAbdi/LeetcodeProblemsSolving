class Solution:
    def isHappy(self, n: int) -> bool:
        same = dict()
        while n not in list(same.keys()):
            if n == 1:
                return True
            counter = 0
            for i in range(len(str(n))):
                counter += int(str(n)[i]) ** 2
            same[n] = counter
            n = counter
        return False
        
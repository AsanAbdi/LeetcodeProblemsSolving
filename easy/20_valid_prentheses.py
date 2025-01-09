class Solution:
    def isValid(self, etal: str) -> bool:
        while len(etal) > 0:
            s = len(etal)
            etal = etal.replace('()', '').replace('{}', '').replace('[]','')
            if len(etal) == s: return False
        return True
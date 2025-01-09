class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = ' '
        while last == ' ':
            last = s[-1]
            if last == ' ':
                s = s[:-1]
        return len(s.split(' ')[-1])
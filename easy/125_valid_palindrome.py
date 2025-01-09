class Solution:
    def isPalindrome(self, s: str) -> bool:
        rem = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '?', '-', '_', '+', '=', '/', "\ "[0], '|', '[', ']', '{','}', ':', ';', ',', '.', '"', "'", '~', '`']
        for i in rem:
            s = s.replace(i, '')
        return ''.join(s.split(' ')).lower() == ''.join(s.split(' '))[::-1].lower()
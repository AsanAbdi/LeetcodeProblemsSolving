class Solution:
    def canConstruct(self, s, k):
        if k > len(s):
            return False
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        odd_count = 0
        for count in char_count.values():
            if count % 2 != 0:
                odd_count += 1
        return odd_count <= k
        
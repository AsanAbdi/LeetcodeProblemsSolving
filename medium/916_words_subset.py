from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def char_count(word: str) -> List[int]:
            freq = [0] * 26
            for char in word:
                freq[ord(char) - ord('a')] += 1
            return freq
        max_freq_words2 = [0] * 26
        for word in words2:
            word_freq = char_count(word)
            for i in range(26):
                max_freq_words2[i] = max(max_freq_words2[i], word_freq[i])
        result = []
        for word in words1:
            word_freq = char_count(word)
            if all(word_freq[i] >= max_freq_words2[i] for i in range(26)):
                result.append(word)
        
        return result
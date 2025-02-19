from typing import List

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return len(list(filter(lambda x: x.startswith(pref), words)))
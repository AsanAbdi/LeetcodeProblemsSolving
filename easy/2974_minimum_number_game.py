from typing import List


class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        while nums:
            al = min(nums)
            nums.remove(al)
            bob = min(nums)
            nums.remove(bob)
            arr.append(bob)
            arr.append(al)
        return arr
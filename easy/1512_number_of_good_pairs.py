from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = []
        for i in range(len(nums)):
            for s in range(i):
                if nums[i] == nums[s]:
                    answer.append('1')
        return len(answer)
        
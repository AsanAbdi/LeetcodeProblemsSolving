from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        answer = nums[0]
        for i in list(set(nums)):
            answer = i if nums.count(i) >= nums.count(answer) else answer
        return answer
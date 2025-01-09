from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lest = []
        for i in range(len(nums)-1):
            for l in range(len(nums)):
                if nums[i] + nums[l] == target and l != i:
                    lest.append(nums.index(nums[i]))
                    nums[i] += 1
                    if nums.index(nums[l]) not in lest:
                        lest.append(nums.index(nums[l]))
                        return lest
                    else:
                        return [nums.index(nums[i]), nums.index(nums[i])+1]
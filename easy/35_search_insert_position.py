class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        answer = 0
        for i in range(len(nums)):
            if nums[i] == target:
                answer = nums.index(nums[i])
                break
            elif nums[i] > target:
                if i == 0:
                    answer = 0
                    break
                elif nums[i-1] < target:
                    answer = i
                    break
            elif nums[i] < target:
                if i+1 == len(nums):
                    answer = i+1
                else:
                    continue
        
        return answer
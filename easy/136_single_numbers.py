from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = False
        for i in range(len(nums)):
            arr = nums[:]
            try:
                arr.remove(nums[i])
                arr.remove(nums[i])
                if len(arr) == 1:
                    print(arr)
                    answer = arr[0]
                    break
            except:
                answer = nums[i]
        
        return answer if str(answer)[0] != 'F' else nums[0]
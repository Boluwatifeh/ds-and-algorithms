# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i, num in enumerate(nums):
            for j in range(i+1, len(nums)):
                if nums[i] +  nums[j] == target:
                    return [i, j]
        return None
                    
    
test = Solution()
print(test.twoSum([2,7,11,15], 9)) #output -> [0,1]
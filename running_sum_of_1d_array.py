# https://leetcode.com/problems/running-sum-of-1d-array/submissions/

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = [nums[0]]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            result.append(nums[i])
        return result
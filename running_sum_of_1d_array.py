# https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result = [nums[0]]
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
            result.append(nums[i])
        return result
# test input [1,2,3,4] -> output [1, 3, 7, 10] i.e [1, 1+2, 1+2+3, 1+2+3+4]
test = Solution()
print(test.runningSum([1,2,3,4]))
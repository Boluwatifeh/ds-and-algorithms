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


#using list comprehension note that this takes O(n^2) this is because of the for loop and the sum() function being called.
def running_sum(nums: list[int]) -> list[int]:
    return [sum(nums[:i+1]) for i in range(len(nums))] 
#test input [2,34,6,9,7] -> expected output [2, 36, 42, 51, 58]
verify = running_sum([2,34,6,9,7])
print(verify)

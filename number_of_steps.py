# Given an integer num, return the number of steps to reduce it to zero.

# In one step, if the current number is even, you have to divide it by 2, 
# otherwise, you have to subtract 1 from it.
# Input: num = 14
# Output: 6
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0

        while num > 0:
            if num % 2 == 0:
                num = num//2
                count +=1
            else:
                num = num - 1
                count +=1
        return count

testcase = Solution()
print(f"{testcase.numberOfSteps(14)}")
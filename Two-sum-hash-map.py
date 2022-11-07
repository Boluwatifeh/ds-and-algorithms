class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        complement_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement  in complement_dict:
                return [complement_dict[complement], i] 
            else:
                complement_dict[num] = i

verify = Solution()
# input -> nums = [2,7,4,0,3], target: 9 
# output = nus[0] + nums [1] -> [0,1]
print(verify.twoSum([2,7,4,0,3], 9))
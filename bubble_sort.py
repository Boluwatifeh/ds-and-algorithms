def bubble_sort(nums:list[int]):
    for j in range(len(nums)):
        for i in range(len(nums)-1):
            print(nums[i], nums[i+1])
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
            print(nums[i], nums[i+1])
            
    return nums
            


num = [5, 8, 2, 6, 34, 10, 1, 0]

print(bubble_sort(num))
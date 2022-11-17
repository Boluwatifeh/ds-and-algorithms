def bubble_sort(nums:list[int]):
    for i in range(len(nums)):
        for j in range(len(nums)-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return (f"sorted list in ascending order -> {nums}")
            


num = [5, 8, 2, 6, 34, 10, 1, 0]

print(bubble_sort(num))
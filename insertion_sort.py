def insertionSort(arr:list[int]):
    for i in range(1, len(arr)):
        anchor = arr[i]
        j = i - 1 
        while j>=0 and anchor < arr[j]:
            arr[j+1] = arr[j]
            j = j - 1 
        arr[j+1] = anchor


nums = [ 54, 23, 7, 3, 1, 19, 79, 91, 12]

insertionSort(nums)
print(nums)
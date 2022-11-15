# Implment selection sort algorithm
def selectionSort(unsorted_list):
    for i in range(len(unsorted_list)):
        min_val = i
        for j in range(i+1, len(unsorted_list)):
            if unsorted_list[j] < unsorted_list[i]:
                min_val = j
        unsorted_list[i], unsorted_list[min_val] = unsorted_list[min_val], unsorted_list[i]
    

nums = [5,3,8,6,7,2]
selectionSort(nums)
print(nums)
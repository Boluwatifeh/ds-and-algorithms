def binary_search(list: list[int], target:int):
    first = 0 # this is our counter for the loop which keeps track of the first element at each iteration
    last = len(list) - 1 # this keeps track of the last element
    while first <= last:
        mid = (first +  last) // 2 # this keeps track of the midpoint of our list to search on each iteration
        if target == list[mid]: # if target is equal to our midpoint, exit loop, this is a complexity O(n)
            return mid
        elif target > list[mid]: # this checks if our target is greater than than the number at the midpoint, if yes, eliminate the list preceding the midpoint by updating our first counter to point to midpoint+1
            first = mid+1
        else:
            last = mid - 1 # this checks if our target is lower than the number at the midpoint, if yes, we need to elimiinate the list after our midpoint by updating our last counter
    return None

numbers = [1,2,3,4,5,6,7,8,9]
test = binary_search(numbers, 12)


def verify(index):
    if index  is not None:
        print("Target is found at index", index)
    else:
        print("Target is not found in list")

verify(test)



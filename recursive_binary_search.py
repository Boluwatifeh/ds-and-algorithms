def recursive_binary_search(list: list[int], target):
    if len(list) == 0:
        return False
    else:
        mid = (len(list) // 2)
        if target == list[mid]:
            return True
        else:
            if target > list[mid]:
                return recursive_binary_search(list[mid+1:], target)
            else:
                return recursive_binary_search(list[:mid-1], target)

def verify(result):
    if result:
        print("Target found")
    else:
        print("Target not found")



numbers = [1,2,3,4,5,6,7,8,9]
result = recursive_binary_search(numbers, 2)
verify(result)

result = recursive_binary_search(numbers, 15)
verify(result)
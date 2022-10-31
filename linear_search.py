def linear_search(list: list[int], target:int):
    """
    Returns the index of the target if found, else returns None
    """
    for i, num in enumerate(list):
        if num == target:
            return i 
    return None

numbers = [1,2,3,4,5,6,7,8,9]
test = linear_search(numbers, 6)


def verify(index):
    if index  is not None:
        print("Target is found at index", index)
    else:
        print("Target is not found in list")

verify(test)

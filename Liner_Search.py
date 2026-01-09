def linear_search(arr, target):
    for index in range(len(arr)):    # Traverse through all elements in the array
        if arr[index] == target:     # If the element is found, return its index
            return index
    return -1                         # If the element is not found, return -1
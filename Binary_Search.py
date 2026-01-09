def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:                # If x is greater, ignore left half
            low = mid + 1
        elif arr[mid] > x:              # If x is smaller, ignore right half
            high = mid - 1
        else:                           # means x is present at mid
            return mid

    return -1                           # If we reach here, then the element was not present
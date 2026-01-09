def bubble_sort(array):

    passes = 1
    swapped = True

    while swapped == True: # If zero swaps occur in a loop, then it's already sorted
        swapped = False
        for i in range(len(array) - passes):# Iterate through the list n times, ignoring last items as they have already been sorted
            if array[i+1] > array[i]:       # Swap elements if they are in the wrong order
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
                swapped = True              # Mark that a swap has occurred
        passes += 1
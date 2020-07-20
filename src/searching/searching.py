def linear_search(arr, target):
    search = -1 # return -1 if not found
    index = 0   # keep track of index
    # Loop through arr
    for item in arr:
        # if item in arr is == target
        if item == target:
            # update search
            search = index
        # update index after each loop
        index += 1
    return search
    

# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Find item in the middle
    # if middle == target
        # return True
    # else if middle < target
        # eliminate left half
        # repeat search
    # else if middle > target
        # eliminate right half
        # repeat search
    return -1  # not found



# sorted list
arr = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
target = 19
print("Linear:", linear_search(arr, target))
print("Binary:", binary_search(arr, target))
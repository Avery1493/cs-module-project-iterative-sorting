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
    # Find high and low index
    high = len(arr) -1
    low = 0
    
    while low <= high:
        middle = (low + high ) // 2
        guess = arr[middle]
        
        # if guess == target
        if guess == target:
            return middle
        # else if guess > target
        elif guess > target:
            high = middle -1
        # else if guess < target
        elif guess < target:
            low = middle + 1
    return -1


# sorted list
arr = [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]
target = 19
print("Linear:", linear_search(arr, target))
print("Binary:", binary_search(arr, target))
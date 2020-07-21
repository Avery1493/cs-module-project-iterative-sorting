# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for element in range(cur_index + 1, len(arr)):
            if arr[element] < arr[smallest_index]:
                smallest_index = element

        # TO-DO: swap
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # iterate through arr
    for i in range(0, len(arr)):
        # inner loop to repeat and decrement len(arr)
        for j in range(1, len(arr) - i):
        # if first element > second element
            if arr[j-1] > arr[j]:
                # swap
                arr[j-1], arr[j] = arr[j], arr[j-1]  
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr


arr = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
arr2 = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
print("Selection:", selection_sort(arr))
print("Bubble:", bubble_sort(arr2))

# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    num_elements = len(arrA) + len(arrB)
    merged_arr = []
    
    # Setting left and right index
    left = 0
    right = 0
    
    # Loop through if left < len of arrA and right < len of arrB
    while left < len(arrA) and right < len(arrB):
        # If the left index of arrA is <= the right index of arrB
        if arrA[left] <= arrB[right]:
            # Append the left index of arrA to the merged_arr list
            merged_arr.append(arrA[left])
            # Increment the left index 
            left += 1
        else:
            # Append the right index of arrB to the merged_arr list
            merged_arr.append(arrB[right])
            # Increment the right index
            right += 1
    # Checking for remaining values to the left
    while left < len(arrA):
        # Append the left index of arrA to the merged_arr list
        merged_arr.append(arrA[left])
        # Increment the left index
        left += 1
    # Checking for remaining values to the right 
    while right < len(arrB):
        # Append the right index of arrB to the merged_arr list
        merged_arr.append(arrB[right])
        # Increment the right index
        right += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Find the middle index (floored)
    mid = len(arr) // 2
    # Seperate into lists, left and right, using the middle index
    left = arr[:mid]
    right = arr[mid:]
    # Base case, if an array contains 1 value or less, its already sorted
    if len(arr) <= 1:
        return arr
    else:
        # Recursively split list into left and right until there
        # is only one element in both lists
        return merge(merge_sort(left), merge_sort(right))

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
#def merge_in_place(arr, start, mid, end):
    # Your code here


#def merge_sort_in_place(arr, l, r):
    # Your code here


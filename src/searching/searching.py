# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Check base case; as long as start value is <= end value
    while start <= end:
        # Set the mid index by taking the whole array and flooring it
        mid = (start + end) // 2
        # If target matches the mid index, return that value
        if arr[mid] == target:
            return mid
        # Else if x is less than the mid element, then x can only lie in left
        # half subarray after the mid element. So we recur for left half.
        elif arr[mid] < target:
            return binary_search(arr, target, mid+1, end)
        # Else (x is greater) recur for the right half.
        else:
            return binary_search(arr, target, start, mid-1)
    # If target isn't present in the array
    else:
        return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

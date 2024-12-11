def binary_search(arr, target):
    # Define the initial left and right pointers
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # Find the middle index
        mid = (left + right) // 2
        
        # Check if the target is at the middle
        if arr[mid] == target:
            return mid  # Return the index of the target
        
        # If the target is smaller, ignore the right half
        elif arr[mid] > target:
            right = mid - 1
        
        # If the target is larger, ignore the left half
        else:
            left = mid + 1
    
    # Target not found
    return -1

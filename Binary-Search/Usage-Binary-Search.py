arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

result = binary_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found in the array")

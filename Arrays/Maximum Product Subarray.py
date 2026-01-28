# Find maximum product subarray

# Time Complexity: O(n²)
# Reason: Two nested loops - outer loop iterates n times, inner loop iterates up to n times
# Each multiplication operation is O(1), so overall O(n²)

# Space Complexity: O(1)
# Reason: Only using a constant amount of extra space (product variable)
# The input array is modified in-place, no additional data structures used

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))

def max_product_subarray(arr):
    for i in range(len(arr)):
        product=1
        for j in range(i, len(arr)):
            product *= arr[j]
            arr[i]=max(arr[i], product)
    return arr

print("The maximum product subarray is:", max(max_product_subarray(arr)))
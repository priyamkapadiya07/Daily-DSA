# Find if there is any subarray with sum equal to 0

# Method-1: Brute Force Approach
# Time Complexity: O(n²) - Two nested loops iterate through all subarrays
# Space Complexity: O(n) - Space required to store the returned subarray
# Reason: We check every possible subarray by maintaining a running sum for each starting position

def has_zero_sum_subarray(arr):
    for i in range(len(arr)):
        curr_sum = 0
        for j in range(i, len(arr)):
            curr_sum += arr[j]
            if curr_sum == 0:
                return arr[i:j+1]
    return "No Element"

arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
print(has_zero_sum_subarray(arr))
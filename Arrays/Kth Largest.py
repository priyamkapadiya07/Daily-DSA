# Kth Largest Element in an Array

# Time Complexity: O(n log n) | Space Complexity: O(1)
# Reason: Sorting takes O(n log n) time. Array is sorted in-place.

def kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]

arr = list(map(int, input("Enter elements of array separated by space: ").split()))
k = int(input("Enter the value of k: "))

print(f"The {k}th largest element is:", kth_largest(arr, k))
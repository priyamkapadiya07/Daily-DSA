# Count Inversions

"""
Time Complexity: O(n²)
Reason: The nested loops iterate through all pairs of elements in the array to compare them.
        The outer loop runs n-1 times and the inner loop runs (n-i-1) times on average,
        resulting in a total of (n-1 + n-2 + ... + 1) = n(n-1)/2 comparisons, which is O(n²).

Space Complexity: O(1)
Reason: The algorithm uses only a constant amount of extra space. We only use the variable 'c'
        to count inversions, regardless of the input size. No additional data structures are used.
"""

def count_inversions(arr):
    c = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                c += 1
    return c

arr = list(map(int, input("Enter elements of array separated by space: ").split()))
print(count_inversions(arr))
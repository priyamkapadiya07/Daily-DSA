'''
Chocolate Distribution Problem

Time Complexity: O(n log n)
  - Sorting the array: O(n log n)
  - Linear scan through array: O(n)
  - Overall dominated by sorting operation

Space Complexity: O(1)
  - No extra data structures used (apart from input array)
  - Only using a few variables for computation
'''

def findMinDiff(arr, n, m):
    if m == 0 or n == 0:
        return 0

    arr.sort()

    if n < m:
        return -1

    min_diff = arr[m - 1] - arr[0]

    for i in range(m, n):
        min_diff = min(min_diff, arr[i] - arr[i - m + 1])

    return min_diff

arr = list(map(int, input("Enter chocolate packet sizes separated by space: ").split()))
m = int(input("Enter number of students: "))
n = len(arr)
result = findMinDiff(arr, n, m)
print("Minimum difference is", result)
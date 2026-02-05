# Smallest Subarray with sum greater than a given value

"""
TIME COMPLEXITY: O(n)
REASON: The sliding window algorithm visits each element at most twice:
- The 'end' pointer traverses the array once from index 0 to n-1
- The 'start' pointer only moves forward and never goes backward
- Combined, both pointers move through the array exactly once
- All operations inside the loops (addition, subtraction, comparison) are O(1)

SPACE COMPLEXITY: O(1)
REASON: The function uses only a constant amount of extra space:
- min_length, current_sum, start, n variables are integers
- No additional data structures (arrays, lists, dictionaries, etc.) are used
- The space used is independent of the input size
"""

def smallest_subarray(arr, x):
    n = len(arr)
    min_length = n + 1
    current_sum = 0
    start = 0

    for end in range(n):
        current_sum += arr[end]

        while current_sum > x:
            min_length = min(min_length, end - start + 1)
            current_sum -= arr[start]
            start += 1

    return min_length if min_length <= n else 0

arr=list(map(int, input("Enter array elements separated by space: ").split()))
x=int(input("Enter the value of x: "))
result = smallest_subarray(arr, x)
if result > 0:
    print(f"The length of the smallest subarray with sum greater than {x} is: {result}")
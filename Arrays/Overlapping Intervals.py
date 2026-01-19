# Merge Intervals

# Time Complexity: O(n log n)
#   - Sorting the intervals takes O(n log n) where n is the number of intervals
#   - The single pass through sorted intervals takes O(n)
#   - Overall: O(n log n) due to sorting being the dominant operation
#
# Space Complexity: O(n) or O(1)
#   - O(n) if we count the output merged array (in worst case, no overlaps)
#   - O(1) if we only count auxiliary space (not counting the result)
#   - Sorting in-place may use O(log n) for recursion stack (depending on Python's sort implementation)


def merge_intervals(arr):
    if not arr:
        return []

    # 1. Sort the intervals based on the starting value
    arr.sort(key=lambda x: x[0])

    merged = []
    
    for interval in arr:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    return merged

# Example Usage:
print(merge_intervals([[1, 3], [2, 4], [6, 8], [9, 10]])) # Output: [[1, 4], [6, 8], [9, 10]]
print(merge_intervals([[6, 8], [1, 9], [2, 4], [4, 7]])) # Output: [[1, 9]]

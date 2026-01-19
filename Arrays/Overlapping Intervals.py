# Merge Intervals

def merge_intervals(arr):
    if not arr:
        return []

    # 1. Sort the intervals based on the starting value
    arr.sort(key=lambda x: x[0])

    merged = []
    
    for interval in arr:
        # 2. If the list of merged intervals is empty or if the current 
        # interval does not overlap with the last merged one, add it.
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # 3. Otherwise, there is an overlap, so we merge the current 
            # interval with the last merged one by updating its end time.
            merged[-1][1] = max(merged[-1][1], interval[1])
            
    return merged

# Example Usage:
print(merge_intervals([[1, 3], [2, 4], [6, 8], [9, 10]])) # Output: [[1, 4], [6, 8], [9, 10]]
print(merge_intervals([[6, 8], [1, 9], [2, 4], [4, 7]])) # Output: [[1, 9]]

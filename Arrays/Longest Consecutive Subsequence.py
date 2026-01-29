# Find longest consecutive subsequence

"""
TIME COMPLEXITY: O(n²)
    - Converting to set and sorting: O(n log n)
    - Nested loops: O(n²) in worst case (outer loop runs n times,
      inner loop can run up to n times for each iteration)
    - Overall dominated by nested loops
    
SPACE COMPLEXITY: O(n)
    - Dictionary 'd' stores at most n elements: O(n)
    - Temporary array 'a1' can store up to n elements: O(n)
    - Set conversion also uses O(n) space
    - Overall space used is O(n)
"""

arr = [2, 6, 1, 9, 4, 5, 3]
arr = list(set(sorted(arr)))

d = {}
for i in range(len(arr)):
    a1 = []
    broken = False

    for j in range(i, len(arr) - 1):
        if arr[j] + 1 == arr[j + 1]:
            a1.append(arr[j])
        else:
            broken = True
            break

    if not broken:
        a1.append(arr[j + 1])
    else:
        a1.append(arr[j])

    d[len(a1)] = a1

max_key = max(d.keys())
print("The longest consecutive subsequence is:", d[max_key])
# Merge 2 sorted arrays without using Extra space.

a = [2, 4, 7, 10]
b = [2, 3]
# Approach: Combine both arrays and sort them.

# Time Complexity: O((n+m) * log(n+m))
#   Reason: Concatenating creates new array O(n+m), then Python's sort uses Timsort O((n+m)*log(n+m))
# Space Complexity: O(n+m)
#   Reason: Concatenation (a+b) creates a new array with all elements from both arrays
print(sorted(a+b))

# -----------------------------------------------------------------------------------------------------------------------------------

# Optimal Approach: Start from the end of first array and beginning of second array.

# Time Complexity: O(n*log(n) + m*log(m))
#   Reason: While loop runs O(min(n,m)) times, but sorting dominates. a.sort() is O(n*log(n)) and b.sort() is O(m*log(m))
# Space Complexity: O(1)
#   Reason: Only swapping elements in existing arrays, no new data structures created (sort uses O(1) space on average)
def merge_array(a,b):
    i=len(a)-1
    j=0
    while i>=0 and j<len(b):
        if a[i]>b[j]:
            a[i],b[j]=b[j],a[i]
            i-=1
            j+=1
        else:
            break
    a.sort()
    b.sort()
    return a,b
print(merge_array(a,b))
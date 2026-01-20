# Next Permutation

def next_permutation(arr):
    """
    Time Complexity: O(n)
    Reason: We traverse the array from right to left (worst case n iterations),
    swap one element (O(1)), and reverse a portion of the array (at most n/2 iterations).
    All operations combined are O(n).
    
    Space Complexity: O(1)
    Reason: We only use constant extra space for variables (n, i, j, left, right).
    The algorithm modifies the input array in-place without using any additional data structures.
    """
    n = len(arr)
    i = n - 2

    # Step 1: Find the first decreasing element from the end
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i >= 0:
        # Step 2: Find the element just larger than arr[i] to swap with
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]

    # Step 3: Reverse the elements after index i
    left, right = i + 1, n - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

arr = [2, 4, 1, 7, 5, 0]
print(next_permutation(arr))  # Output: [2, 4, 5, 0, 1, 7]


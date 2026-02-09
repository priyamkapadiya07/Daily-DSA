def median(arr):
    """
    Return the median of `arr`.

    Time Complexity: O(n log n)
    Reason: Sorting the array with `arr.sort()` dominates runtime (O(n log n)).

    Space Complexity: O(1) extra (in-place)
    Reason: Sorting is performed in-place and only O(1) extra variables are used.
    """
    arr.sort()
    n = len(arr)

    if n % 2 == 0:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (arr[mid1] + arr[mid2]) / 2
    else:
        mid = n // 2
        return arr[mid]


if __name__ == "__main__":
    arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    print(median(arr))
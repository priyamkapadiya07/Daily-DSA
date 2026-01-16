# Minimize the maximum difference between heights

def get_min_diff(arr, k):
    n = len(arr)
    if n == 1:
        return 0

    arr.sort()

    ans = arr[-1] - arr[0]

    for i in range(1, n):
        # If negative height, skip
        if arr[i] - k < 0:
            continue

        min_height = min(arr[0] + k, arr[i] - k)
        max_height = max(arr[i - 1] + k, arr[-1] - k)

        ans = min(ans, max_height - min_height)

    return ans

arr = list(map(int, input("Enter elements of array separated by space: ").split()))
k = int(input("Enter the value of k: "))
print("The minimized maximum difference between heights is:", get_min_diff(arr, k))

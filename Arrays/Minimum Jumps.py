# Minimum no. of Jumps to reach end of an array

def min_jumps(arr):
    n = len(arr)

    if n <= 1:
        return 0

    if arr[0] == 0:
        return -1

    maxReach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, n):
        # Reached the end
        if i == n - 1:
            return jumps

        maxReach = max(maxReach, i + arr[i])
        steps -= 1

        # Need to make another jump
        if steps == 0:
            jumps += 1

            # If cannot move further
            if i >= maxReach:
                return -1

            steps = maxReach - i

    return -1
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
result = min_jumps(arr)
if result != -1:
    print("Minimum number of jumps to reach the end is:", result)   
else:
    print("Cannot reach the end of the array.")

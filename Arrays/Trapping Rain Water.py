'''Trapping Rain water problem'''

# Method 1: Using precomputed arrays for left max and right max
def trap(arr):
    n = len(arr)
    if n == 0:
        return 0

    leftMax = [0] * n
    rightMax = [0] * n

    leftMax[0] = arr[0]
    for i in range(1, n):
        leftMax[i] = max(leftMax[i - 1], arr[i])

    rightMax[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], arr[i])

    water = 0
    for i in range(n):
        water += min(leftMax[i], rightMax[i]) - arr[i]

    return water
arr = list(map(int, input("Enter elevation map elements separated by space: ").split()))
result = trap(arr)
print("Total trapped rain water:", result)
    
# Method 2: Two-pointer approach (commented out)
# def trap(arr):
#     left = 0
#     right = len(arr) - 1
#     leftMax = rightMax = 0
#     water = 0

#     while left < right:
#         if arr[left] < arr[right]:
#             leftMax = max(leftMax, arr[left])
#             water += leftMax - arr[left]
#             left += 1
#         else:
#             rightMax = max(rightMax, arr[right])
#             water += rightMax - arr[right]
#             right -= 1

#     return water

# arr = [3,0,1,0,4,0,2]
# result = trap(arr)
# print("Total trapped rain water:", result)
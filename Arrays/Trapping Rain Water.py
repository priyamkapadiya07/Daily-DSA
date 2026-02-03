'''Trapping Rain water problem'''
a=[3,0,1,0,4,0,2]
l=a
r=a
# left max
for i in range(len(a)-1):
    if l[i]>l[i+1]:
        l[i+1]=l[i]
print(l)

# right max
for j in range(len(r)-1,0,-1):
    if r[j-1]<r[j]:
        r[j-1]=r[j]
print(r)

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
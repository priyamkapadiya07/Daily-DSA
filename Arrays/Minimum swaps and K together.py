# Minimum swaps required bring elements less equal K together

a=[2,7,9,5,8,7,4]
k=6
# def min_swaps(arr, k):
#     count = 0
#     for i in range(len(arr)):
#         if arr[i] <= k:
#             count += 1

#     bad = 0
#     for i in range(count):
#         if arr[i] > k:
#             bad += 1

#     ans = bad
#     j = count
#     for i in range(len(arr)):
#         if j == len(arr):
#             break
#         if arr[i] > k:
#             bad -= 1
#         if arr[j] > k:
#             bad += 1
#         ans = min(ans, bad)
#         j += 1

#     return ans

i=0
for j in range(len(a)):
    if a[i]<k:
        i+=1
    elif a[j]<k:
        a[i],a[j]=a[j],a[i]
        i+=1
print(a)
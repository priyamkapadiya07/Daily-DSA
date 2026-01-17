# Find Largest sum contiguous Subarray
# This problem also known as Kadane's Algorithm

# Time Complexity: O(n) | Space Complexity: O(1)
# Reason: Single pass through array with constant space for variables.

arr = list(map(int, input("Enter elements of array separated by space: ").split()))
# d={}

# for i in range(len(arr)):
#     n=i+1
#     while n<=len(arr):
#         subarr=arr[i:n]
#         d[sum(subarr)]=subarr
#         n+=1
# print(d)
# print("\nLargest sum contiguous Subarray is:",d[max(d.keys())],"with sum =",max(d.keys()),"\n")

print("\n----- Optimal Approach (Kadane's Algorithm) -----\n")

max_sum = curr_sum = arr[0]
start = end = temp_start = 0

for i in range(1, len(arr)):
    if arr[i] > curr_sum + arr[i]:
        curr_sum = arr[i]
        temp_start = i
    else:
        curr_sum += arr[i]

    if curr_sum > max_sum:
        max_sum = curr_sum
        start = temp_start
        end = i

print("Largest sum contiguous Subarray is:", arr[start:end+1], "with sum =", max_sum)

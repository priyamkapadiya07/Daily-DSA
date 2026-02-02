'''
Find the triplet that sum to a given value

Time Complexity: O(n^2)
Reason: The outer loop fixes index `i` and runs for about `n` iterations. For each `i`, the inner pointer `p2` (with `p1` fixed as `i+1`) may scan the remaining elements; the total number of checks is roughly sum_{i=0..n-1}(n-i) = O(n^2).

Space Complexity: O(1)
Reason: The algorithm uses a fixed number of extra variables (`i`, `p1`, `p2`, `current_sum`) and no additional data structures proportional to input size.
'''

def findTriplet(arr, target_sum):
    i=0
    n=len(arr)
    for i in range(n-2):
        p1=i+1
        p2=p1+1
        while p2<n:
            current_sum=arr[i]+arr[p1]+arr[p2]
            if current_sum==target_sum:
                return (arr[i], arr[p1], arr[p2])
            p2+=1
arr = list(map(int, input("Enter elements of array separated by space: ").split()))
target_sum = int(input("Enter the target sum: "))
result = findTriplet(arr, target_sum)
if result:
    print("Triplet found:", result)
else:
    print("No triplet found that sums to the target value.") 
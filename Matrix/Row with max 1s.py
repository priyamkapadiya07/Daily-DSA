'''
Find row with maximum no. of 1's

Time Complexity: O(n * m)
For each of the n rows, sum(arr[i]) iterates over m columns.
Space Complexity: O(1)
Only a few variables are used; no extra space proportional to input size.
'''

def row_with_max_1s(arr):
    max_sum=0
    row = 0
    for i in range(len(arr)):
        if max_sum < sum(arr[i]):
            max_sum = sum(arr[i])
            row = i
    return row
arr = [[0,0], [1,1]]
print("Row with maximum 1's is:", row_with_max_1s(arr))
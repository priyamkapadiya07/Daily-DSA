# Find row with maximum no. of 1's

arr = [[0,0], [1,1]]

def row_with_max_1s(arr):
    max_sum=0
    row = 0
    for i in range(len(arr)):
        if max_sum < sum(arr[i]):
            max_sum = sum(arr[i])
            row = i
    return row
print("Row with maximum 1's is:", row_with_max_1s(arr))
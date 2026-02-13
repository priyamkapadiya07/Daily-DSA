# Find median in a row wise sorted matrix
"""
Finds the median in a row-wise sorted matrix by flattening and sorting.

Time Complexity:
    O(m * n) for flattening the matrix (where m = number of rows, n = number of columns),
    plus O(m * n * log(m * n)) for sorting the flattened array.
    Overall: O(m * n * log(m * n)).

Space Complexity:
    O(m * n) for storing the flattened array.
    The original matrix is not modified, but an extra list is used for sorting.

Reason:
    - Flattening requires traversing all elements.
    - Sorting dominates the complexity due to the use of Python's built-in sort.
    - Space is required for the flattened list.
"""

def median(matrix):
    for i in range(1, len(matrix)):
        mat[0].extend(matrix[i])
    mat[0].sort()
    n = len(mat[0])
    if n % 2 == 0:
        return (mat[0][n // 2 - 1] + mat[0][n // 2]) // 2
    else:
        return mat[0][n // 2]
    
mat = [[2,4,9],[3,6,7],[4,7,10]]
print("Median is:",median(mat))
'''
Search an element in a Matrix

Time Complexity:
The algorithm starts from the top-right corner and moves either left or down in each step.
In the worst case, it will traverse at most one full row and one full column (i.e., m + n steps for an m x n matrix).
Therefore, the time complexity is O(m + n).

Space Complexity:
The algorithm uses only a constant amount of extra space (for variables row and col).
No additional data structures are used, so the space complexity is O(1).
'''

def search_matrix(matrix, target):
    row=0
    col=len(matrix[0])-1
    while row<len(matrix) and col>=0:
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]>target:
            col-=1
        else:
            row+=1
    return False

mat = [[1, 5, 9, 11], [14, 20, 21, 26], [30, 34, 43, 50]]
x = 42
print(search_matrix(mat, x))
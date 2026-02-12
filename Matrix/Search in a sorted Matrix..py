# Search an element in a Matrix


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
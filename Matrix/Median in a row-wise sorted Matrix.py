# Find median in a row wise sorted matrix

mat = [[1, 3, 5],[2, 6, 9],[3, 6, 9]]

def median(matrix):
    for i in range(1,len(matrix)):
        mat[0].extend(matrix[i])
    mat[0].sort()
    n = len(mat[0])
    if n%2==0:
        return (mat[0][n//2-1]+mat[0][n//2])//2
    else:
        return mat[0][n//2]
        
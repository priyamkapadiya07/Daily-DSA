# Find median in a row wise sorted matrix


def median(matrix):
    for i in range(1,len(matrix)):
        mat[0].extend(matrix[i])
    mat[0].sort()
    n = len(mat[0])
    if n%2==0:
        return (mat[0][n//2-1]+mat[0][n//2])//2
    else:
        return mat[0][n//2]
    
mat = [[2,4,9],[3,6,7],[4,7,10]]
print("Median is:",median(mat))
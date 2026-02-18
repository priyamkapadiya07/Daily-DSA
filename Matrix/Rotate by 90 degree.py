# Rotate by 90 degree

mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

def rotate90(mat):
    '''
    Time Complexity: O(n^2)
        - The algorithm iterates through each element of the n x n matrix once to perform the rotation.
        - Each element is accessed and assigned to its new position in O(1) time, resulting in O(n^2) for the entire matrix.

    Space Complexity: O(1)
        - The rotation is performed in-place, meaning no additional space is used that scales with the input size.
        - Only a few temporary variables are used for swapping elements, which require O(1) space.
    '''
    n = len(mat)
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    for i in range(n):
        mat[i].reverse()
rotate90(mat)
print("The matrix after rotating by 90 degrees is:")
for row in mat:
    print(row)
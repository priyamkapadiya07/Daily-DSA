''''
Time Complexity: O(N^2 log N)
  - Extracting all elements: O(N^2)
  - Sorting the array: O(N^2 log N)
  - Reassigning sorted values: O(N^2)
  - Dominant term: sorting, so overall O(N^2 log N)

Space Complexity: O(N^2)
  - Uses an auxiliary list 'space' to store all elements (N*N elements)
  - No extra space beyond this list and the input matrix

Print elements in sorted order using row-column wise sorted matrix
'''
def sortedMatrix(N,Mat):
    space=[Mat[i][j] for i in range(N) for j in range(N)]
    space.sort()
    k=0
    for i in range(N):
        for j in range(N):
            Mat[i][j]=space[k]
            k+=1
    return Mat

Mat=[[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
N=4
print("Sorted Matrix is:", sortedMatrix(N, Mat))
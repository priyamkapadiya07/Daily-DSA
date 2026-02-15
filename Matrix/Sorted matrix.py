# Print elements in sorted order using row-column wise sorted matrix

Mat=[[10,20,30,40],[15,25,35,45],[27,29,37,48],[32,33,39,50]]
N=4
def sortedMatrix(N,Mat):
    space=[Mat[i][j] for i in range(N) for j in range(N)]
    space.sort()
    k=0
    for i in range(N):
        for j in range(N):
            Mat[i][j]=space[k]
            k+=1
    return Mat

print("Sorted Matrix is:", sortedMatrix(N, Mat))
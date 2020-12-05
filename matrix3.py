def matrix(arr):
    mat = []
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            mat.append(arr[i][j])

    # return mat
    mat.sort()

    if len(mat)%2 == 0:
        return (mat[len(mat)//2] + mat[(len(mat)//2) + 1])//2
    else:
        return mat[len(mat)//2]

print(matrix([[1], [2], [3]]))               




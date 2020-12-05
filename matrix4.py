def matrix(arr):
    mat = []
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                count += 1
        mat.insert(i, count)
    return mat.index(max(mat)) 

print(matrix([[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]))        
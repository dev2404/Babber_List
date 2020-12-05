import sys
inf = sys.maxsize

def youngify(mat, i, j,n):
    rightval = mat[i][j+1] if j + 1 < n else inf
    downval = mat[i+1][j] if i + 1 < n  else inf 

    if rightval == inf and downval == inf:
        return
    
    if downval < rightval:
        mat[i][j] = downval
        mat[i+1][j] = inf
        youngify(mat, i+1, j, n)
    else:
        mat[i][j] = rightval
        mat[i][j+1] = inf
        youngify(mat, i, j+1,n)

def extractmin(mat,n):
    ret = mat[0][0]
    mat[0][0] = inf
    youngify(mat, 0,0,n)
    return ret


array = [[10, 20, 30, 40], [15, 25, 35, 45], [27, 29, 37, 48], [32, 33, 39, 50]]
n = len(array)
i=0
while i < n*n:
    print(extractmin(array, n), end="")
    i += 1    
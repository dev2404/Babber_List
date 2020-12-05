def difference(arr):
    maxval = 0
    for a in range(len(arr)-1):
        for b in range(len(arr)-1):
            for c in range(a+1, len(arr)):
                for d in range(b+1, len(arr)):
                    if maxval < int(arr[c][d] - arr[a][b]):
                        maxval = int(arr[c][d] - arr[a][b])
    return maxval

mat = [[ 1, 2, -1, -4, -20 ], [ -8, -3, 4, 2, 1 ], [ 3, 8, 6, 1, 3 ], [ -4, -1, 1, 7, -6 ], [ 0, -4, 10, -5, 1 ]]

print(difference(mat))


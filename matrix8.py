def rotate(arr):
    for row in range(len(arr)):
        for col in range(row, len(arr)):
            arr[row][col], arr[col][row] = arr[col][row], arr[row][col]
    return reverse(arr)        

def reverse(arr):

    for i in range(len(arr)):
        start = 0
        end = len(arr)-1

        while start < end:
            arr[i][start], arr[i][end] = arr[i][end],arr[i][start]
            start += 1
            end -= 1 
    return arr        



arr = [ [ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ] ]
print(rotate(arr))
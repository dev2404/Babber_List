def matrix(arr, target):
    row = len(arr)
    col = len(arr[0])

    if row == 0:
        return False
    if col == 0:
        return False
    if target > arr[-1][-1] and target < arr[0][0]:
        return False

    i = 0
    j = (row * col) -1 
    while i <= j:
        mid = i + (j - i)//2
        c = mid % col
        r = mid // col       
        if arr[r][c] == target:
            return True
        elif arr[r][c] < target:
            i = mid + 1
        else:
            j = mid - 1
    return False        


print(matrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13 ))
                        

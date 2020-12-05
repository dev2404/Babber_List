def rotate(arr, k):
    for i in range(k):
        temp = arr.pop()
        arr.insert(0, temp)
    return arr

arr = [9 ,8 ,7 ,6 ,4 ,2 ,1 ,3]
k = 1
print(rotate(arr, k))        
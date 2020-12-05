def merge(arr1, arr2): 
    arr1 = arr1 + arr2
    return sorted(arr1)

arr1 = [1,3,5,7]
arr2 = [0,2,6,8,9]
print(merge(arr1, arr2))
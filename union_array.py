def union(arr1,arr2):
    arr = []
    arr1 = set(arr1)
    for i in arr2:
        if i not in arr1:
            arr1.add(i)
        else:
            arr.append(i)    
    return len(arr1), arr1, arr        


arr1 = [23, 15, 2, 14, 14, 16, 20 ,52]
arr2 = [2, 48, 15, 12, 26, 32, 47, 54]
print(union(arr1,arr2))

# Pythonic-solution
# t = list(set(arr1) | set(arr2))
# print(t)
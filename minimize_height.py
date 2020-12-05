def minimize_height(arr,k):
    t = arr[0]
    t2 = arr[len(arr)-1]
    t += k-t
    t2 = t2-k
    return t2-t, t, t2
arr = [1, 10, 15]
k = 3
print(minimize_height(arr, k))


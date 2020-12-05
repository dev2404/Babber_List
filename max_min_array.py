# def min_max(arr):
#     mini = maxi = 0
#     for i in range(len(arr)-1):
#         if arr[i] > arr[i+1]:
#             mini = min(mini, arr[i+1])
#             maxi = max(arr[i], maxi)
#         else:
#             mini = min(arr[i],mini)
#             maxi = max(arr[i+1],maxi) 
#     return mini,maxi        

class pair:
    def __init__(self):
        self.max = 0
        self.min = 0

def min_max(arr,n):
    minmax = pair()
    if n == 0:
        minmax.max = arr[0]
        minmax.min = arr[0]
        return minmax
    if n == 2:
        if arr[0] > arr[1]:
            minmax.max = arr[0]
            minmax.min = arr[1]
        else:
            minmax.max = arr[1]
            minmax.min = arr[0]

    for i in range(2, n):
        if arr[i] > minmax.max:
            minmax.max = arr[i]
        elif arr[i] < minmax.min:
            minmax.min = arr[i]
    return minmax.min, minmax.max        

arr = [1000, 11, 445, 1, 330, 3000]
arr_size = 6
print(min_max(arr, arr_size))    
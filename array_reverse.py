def reverse(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverse(arr, start+1, end-1)
    return arr

arr = [1,2,3,4,5,6,7,8,9]
# print(reverse(arr,0,len(arr)-1))

def slicing(arr):
    return arr[::-1]

print(slicing(arr))

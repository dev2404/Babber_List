#code
def subarray(arr):
    currmax = maxi = arr[0]
    for i in arr[1:]:
        currmax = max(currmax+i, i)
        maxi = max(currmax, maxi)
    return maxi

t = int(input())
for i in range(t):
    size = int(input())
    arr = list(map(int, input().split()))
    print(subarray(arr))
    
def jumps(arr,n):
    c = 1
    i = 0
    end = arr[0]
    while i < len(arr):
        i += arr[0]
        c += 1
    return c    

t = int(input())
for i in range(t):
    size = int(input())
    arr = list(map(int, input().strip().split()))
    
    print(jumps(arr, size))    88dd446c7c3a64825bc07583ab4d2499
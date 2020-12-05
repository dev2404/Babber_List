def solve(arr, n):
    import heapq
       
    arr.sort()    
    a, b = 0,0
            
    for i in range(n):
        if i % 2 != 0:
            a = a * 10 + arr[i]
        else:
            b  = b * 10 + arr[i]
    return a+b

print(solve([5, 3, 0, 7, 4], 5))
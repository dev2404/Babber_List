# solution-1
def triplet(arr, n, k):
    count = 0
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for x in range(j+1, n):
                if arr[i]+arr[j]+arr[x] == k:
                    return 1
                
    return 0
# Solution-2
def triplet(arr, n, k):
    count = 0
    arr.sort()
    for i in range(0, n-2):
        
        left = i+1
        right = n-1
        
        while left < right:
            if arr[i]+arr[left]+arr[right] == k:
                return 1
            elif arr[i]+arr[left]+arr[right] < k:
                left += 1
            else:
                right -= 1
    return 0            
        
    
T = int(input())
for i in range(T):
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(triplet(arr, n, k))    



def func(arr, size, k):
    n = size // k
    dict = {}
    ans = []

    for i in arr:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for num in dict:
        if dict[num] >= n:
            ans.append(num)
    return ans        
          


t = int(input())
for i in range(t):
    size = int(input())
    k = int(input())
    arr = list(map(int, input().split()))
    print(func(arr, size,k))    


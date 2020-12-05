def matrix(arr):
    dp = dict()
    m =len(arr)
    n = len(arr[0])

    for i in range(n):
        dp[arr[0][i]] = 1

    for i in range(1, m):
        for j in range(n):
            if arr[i][j] in dp.keys() and dp[arr[i][j]] == i:
                dp[arr[i][j]] += 1

                if i == m-1:
                    print(arr[i][j], end=" ")

mat = [[1, 2, 1, 4, 8], 
       [3, 7, 8, 5, 1], 
       [8, 7, 7, 3, 1], 
       [8, 1, 2, 7, 9]] 
  
print(matrix(mat))

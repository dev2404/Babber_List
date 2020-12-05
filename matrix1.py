#code
def matrix(arr):
    if not matrix:
        return []

    rowbeg = 0
    colbeg = 0
    rowend = len(arr)
    colend = len(arr[0])
    res = []    

    while rowbeg < rowend and colbeg < colend:

        for i in range(colbeg, colend):
            res.append(arr[rowbeg][i])

        for i in range(rowbeg+1, rowend-1):
            res.append(arr[i][colend-1])

        if rowbeg != rowend:
            for i in range(colend-1, colbeg-1,-1):
                res.append(arr[rowend-1][i])

        if colbeg != colend:
            for i in range(rowend-2, rowbeg, -1):
                res.append(arr[i][colbeg])
        rowbeg += 1
        rowend -= 1
        colbeg += 1
        colend -= 1
    return res    


            
    
    
t = int(input())
for i in range(t):
    R, C = list(map(int, input().split()))
    mat = []
    for i in range(R):          
        a =[] 
        for j in range(C):      
            a.append(int(input())) 
        mat.append(a)
# arr = [[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15]]

print(matrix(mat))


    # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16


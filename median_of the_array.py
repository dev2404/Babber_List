def median_array(arr1,arr2):
    median = 0
    max_array = arr1 + arr2
    max_array.sort()

    if len(max_array)%2 == 0:
        median = (max_array[len(max_array)//2] + max_array[(len(max_array)//2)-1])//2
    else:
        median = max_array[(len(max_array)//2)]
    return int(median)


t = int(input())
for i in range(t):
    
    arr1 = list(map(int, input().split()))  #[-5, 3, 6, 12, 15]
    arr2 = list(map(int, input().split()))  #[-12, -10, -6, -3, 4, 10]          
    print(median_array(arr1, arr2)) 
#     ar1[] = {-5, 3, 6, 12, 15}
# ar2[] = {-12, -10, -6, -3, 4, 10}




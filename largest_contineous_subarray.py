def contineous_subarray(arr):
    max_ending_here = 0
    max_so_far = float('-inf') 
    for i in arr:
        max_ending_here = max_ending_here + i
        if max_ending_here < i:
            max_ending_here = i
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
    return max_so_far            

arr = [1 ,2 ,3 ,-2 ,5] 
print(contineous_subarray(arr))   
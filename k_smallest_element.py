import heapq as hp

def k_smallest(arr,k):
    # return hp.nsmallest(k, arr)
    q = []
    for i in range(len(arr)):
        hp.heappush(q,-1 * arr[i])
        if len(q) > k:
            hp.heappop(q)

    # for i in range(k):
    #     temp = hp.heappop(q)      
    #  [hp.heappop(q) for i in range(len(q))]   
    return [hp.heappop(q) for i in range(len(q))] 

arr = [7, 10, 4, 3, 20, 15] 

k = 4

print(k_smallest(arr,k))
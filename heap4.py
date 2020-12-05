import heapq as hp

def kLargest(arr, n, k):
	# code here
    q = []
    for i in range(n):
        hp.heappush(q, arr[i])
        if len(q) > k:
            hp.heappop(q)
    q.sort(reverse=True)       
    return q[-1]
    
#[hp._heappop_max(q) for i in range(len(q))]  
N = 7
K = 3
Arr = [1, 23, 12, 9, 30, 2, 50, 89]
print(kLargest(Arr, N, K))
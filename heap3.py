import heapq as hp

def sliding(arr,k, n):
    res = []
    i = 0
    j = k-1
    heap = arr[i:j+1]
    hp._heapify_max(heap)
    res.append(heap[0])

    last = arr[i]
    i += 1
    j += 1
    nexts = arr[j]

    while j < n:
        heap[heap.index(last)] = nexts

        hp._heapify_max(heap)

        res.append(heap[0])
        last = arr[i]
        i += 1
        j += 1
        if j < n:
            nexts = arr[j]
    return res        

n, k = 10, 3
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sliding(arr, k, n))             

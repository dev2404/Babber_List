import heapq as hp

def merge_bin(arr1, arr2, n1, n2):
    q = []
    for i in arr1:
        q.append(i)

    for i in arr2:
        q.append(i)  

    hp._heapify_max(q)    

    return q

t = int(input())
for i in range(t):
    n1, n2 = list(map(int, input().split()))
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    print(merge_bin(arr1, arr2, n1, n2))




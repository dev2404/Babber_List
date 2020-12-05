# import heapq as hp

# def move_negative_element(arr):
#     q = []
#     for i in range(len(arr)):
#         hp.heappush(q, arr[i])

#     return [hp.heappop(q) for i in range(len(q))]    

arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
# print(move_negative_element(arr))
pos = []
neg = []

for i in arr:
    if i<0:
        neg.append(i)
    else:
        pos.append(i)
print(neg+pos)        

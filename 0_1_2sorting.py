def sorting(arr):
    zero = one = two = 0
    for i in arr:
        if i == 0:
            zero += 1
        elif i == 1:
            one += 1
        else:
            two += 1 

    for i in range(zero):
        arr.remove(0)
        arr.append(0)
    for i in range(one):
        arr.remove(1)
        arr.append(1)
    for i in range(two):
        arr.remove(2)
        arr.append(2)  
    return arr          

arr = [0 ,2, 1, 2, 0]
print(sorting(arr))
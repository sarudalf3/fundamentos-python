def BubbleSort(arr):
    for ord in range(len(arr)-1,0,-1):
        for idx in range(0, ord):
            if arr[idx] > arr[idx+1]:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
    return arr
print(BubbleSort([9,3,5,7,3,2,8,1,0]))
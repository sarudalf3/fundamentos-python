def order(arr):
    for idx in range(len(arr)-1):
        val = arr.pop(arr.index(min(arr[idx:]),idx))
        arr.insert(idx, val)
    return arr

print(order([23,-5,11,11,19,16,11,31]))

#order by insertion
def InsrtOrder(arr):
    for idx in range(1,len(arr)):
        idxWhile = idx-1
        while((arr[idxWhile] > arr[idx]) & (idxWhile>=0)):
            idxWhile -= 1
        
        val = arr.pop(idx)
        arr.insert(idxWhile+1,val)
    return arr

print(InsrtOrder([8,1,-6,9,8,8,-12,6,-1,0]))

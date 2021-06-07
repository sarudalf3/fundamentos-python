#1- biggie_size
def biggiesize(lst=[]):
    val = [x if x <= 0 else "big" for x in lst]
    return val

print(biggiesize([2,65,3,-2,-3,1,-2]))

#2- positive counts
def positiveCounts(lst=[]):
    if len(lst)>0:
        val = [x for x in lst if x > 0]
        lst[-1] = len(val)
        return lst
    else:
        return None

print(positiveCounts(lst=[2,4,-1,-2,6,8,-3,-1]))

#3- total sum
def TotalSum(lst=[]):
    if len(lst)==0:
        return None
    else:
        return sum(lst)

print(TotalSum([1,3,6,9,4]))

#4- mean 
def mean(lst=[]):
    if len(lst)==0:
        return None
    else:
        return sum(lst)/len(lst)

print(mean([1,3,6,9,4]))

#5- length
def long(lst=[]):
    if len(lst)==0:
        return 0
    else:
        return len(lst)

print(long([1,3,6,9,4]))

#6- Min
def mnmo(lst=[]):
    if len(lst)==0:
        return 0
    else:
        return min(lst)
print(mnmo([1,3,6,9,4]))

#7- Max
def mxmo(lst=[]):
    if len(lst)==0:
        return 0
    else:
        return max(lst)
print(mxmo([1,3,6,9,4]))

#8- Final Analysis
def finalSumm(lst=[]):
    dct = {}
    dct['total'] = TotalSum(lst)
    dct['promedio'] = mean(lst)
    dct['minimo'] = mnmo(lst)  
    dct['maximo'] = mxmo(lst)
    dct['longitud'] = long(lst)
    return dct 

print(finalSumm([2,1,-3,-7,5]))

#9- Reverse
def revList(lst=[]):
    if len(lst)==0:
        return lst
    else:
        return lst[::-1]

print(revList([2,1,-3,-7,5]))
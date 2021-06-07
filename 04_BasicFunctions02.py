#1- Countdown numbers function
def countdown(num=10):
    lst = [*range(num,-1,-1)]
    return lst

print(countdown(12))

#2- print and return
def print_and_return(lst=[1,2]):
    print(lst[0])
    return  lst[1]

print(print_and_return([8,-1]))

#3- First plus length
def first_plus_length(lst=[]):
    if len(lst)==0:
        return None
    else: 
        return lst[0]+len(lst)    

print(first_plus_length([4,1,-1,1,6]))

#4- Greatest second values
def greatestValues(lst=[]):
    if len(lst)<2:
        return False
    else:
        val = [x for x in lst if x > lst[1]]
        print(len(val))
        return val

print(greatestValues(lst=[1,3,5,8,3]))

#5- value and length
def length_and_value(val,lng):
    return [val]*lng

print(length_and_value(1,4))
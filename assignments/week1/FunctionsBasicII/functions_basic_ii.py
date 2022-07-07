# Countdown
from re import A


def countdown(i):
    list=[i]
    while (i>0):
        i= i-1
        list.append(i)
    print(list)
    return list
countdown(10)

# Print and Return
def print_and_return(x):
    print(x[0])
    return x[1]
print_and_return([1,2])

# First plus Length
def first_plus_length(x):
    sum= x[0] + len(x)
    print(sum)
    return sum
first_plus_length([1,2,3,4,5])

#Values greater than second
def values_greater_than_second(x):
    if (len(x) <2):
        print("False")
        return False
    new_list = []
    for i in range(0,len(x)):
        if (x[i]>x[1]):
            new_list.append(x[i])
    print(len(new_list))
    return new_list
print(values_greater_than_second([5,2,3,1,4]))
values_greater_than_second([3])

#This Length, that Value
def length_and_value(size, value):
    list=[]
    for i in range(0, size):
        list.append((value))
    print(list)
    return list
length_and_value(4,7) 
length_and_value(6,2)
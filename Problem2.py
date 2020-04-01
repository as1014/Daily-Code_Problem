#Problem 2

#Given an array of integers
#Return a ew array such that 
#each element at index i of the new array 
# is the product of all the numbers in the original array 
# except the one at i
#

l = [3, 2 , 1]

def sol(lst, size):
    if(size == 0):
        return 0
    else:
        return lst[size - 1] * sol(lst, size - 1)

total = sol(l, len(l))

print("sum is " , total)
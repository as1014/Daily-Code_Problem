#Problem 2

#Given an array of integers
#Return a new array such that 
#each element at index i of the new array 
# is the product of all the numbers in the original array 
# except the one at i
#

l = [1, 2, 3, 4, 5]
lsize = len(l)


def pol(nums):
    #generate prefix products
    pre_prod = []
    for num in nums:
        if pre_prod:
           pre_prod.append(pre_prod[-1]* num)
        else:
            pre_prod.append(num)
    
    #generate suffix products
    suf_prod = []
    for num in reversed(nums):
        if suf_prod:
            suf_prod.append(suf_prod[-1] * num)
        else:
            suf_prod.append(num)
    suf_prod = list(reversed(suf_prod))

    #generate results
    results = []
    for i in range(len(nums)):
        if i == 0:
            results.append(suf_prod[i + 1])
        elif i == len(nums) - 1:
            results.append(pre_prod[i - 1])
        else:
            results.append(pre_prod[i - 1] * suf_prod[i + 1])
    print(results)
    return results

total = pol(l)

print("Products excluding at i is " , total)
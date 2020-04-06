# Problem 4

#Given an array of integers, 
# find the first missing positive integer in linear time and constant space. 
#

#input
l = [3, 4, -1, 1]

def fmp(nums):
    s = set(nums)
    i = 1
    while i in s:
       i += 1
    return i

#run 
ans = fmp(l)

print(ans)
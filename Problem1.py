#problem 1 
#
#Given a list of numbers and a number k
#Return whether any two numbers from the list add up to k

#test values
l = [15, 13, 10 , 7]
k = 17

#will be used for recursion
l_len = len(l)

def sum(lst, k):
    #loop through the list
    for i in range(l_len):
        lst_len = len(lst)
        base_num = lst[0]
        sum_num = 0

        #pop the first item in list
        lst.pop(0)

        #refresh the list without the first one
        lst_len = len(lst)

        for j in range(lst_len):
            sum_num = base_num + lst[j]
           # print(base_num, lst, lst_len, sum_num)

            if sum_num == k:
                #return the values used to match the k value
                return base_num, lst[j]
    
    #return false if nothing matches            
    return False

r = sum(l, k)

if not r:
    print("No matches found!")
else:
    print("there's a match!")
def find_index(mylist, lower, upper, min_ele= math.inf, min_index= math.inf):
    '''
    Objective  : To find the index of minimum element of the sublist from lower to upper-1
    parameters :
        mylist : The list in which the min index is to be found
        lower  : The lower bound for the sublist in which min index is to be found
        upper  : The upper bound for the sublist in which min index is to be found
        min_ele   : The minimum element, default value = infinity
        min_index : Index of the minimum element, default value = infinity

    Return value : min_index - The index of the minimum value
    '''
    # approach : compares the curent minimum element with each element of the supposed sublist,
    # If any element is even smaller than min_ele, it becomes the new minimum.
    # The process repeats until lower bound reaches to upper bound

    if(upper == lower):
        return min_index
    
    if mylist[lower] < min_ele:
        min_ele=mylist[lower]
        min_index=lower
    
    return find_index(mylist,lower+1,upper,min_ele,min_index)


mylist=[9,1,11,4,6,2,0]

# Test case 1
lower=0
upper=len(mylist)
min_index=find_index(mylist,lower,upper)
print(min_index)


# Test case 2
lower=0
upper=len(mylist)-2
min_index=find_index(mylist,lower,upper)
print(min_index)

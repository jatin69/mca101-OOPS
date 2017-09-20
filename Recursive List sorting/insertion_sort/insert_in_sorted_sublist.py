def insertSorted(sorted_list,ele,lower,upper):
    '''
    Objective : Insert an element in the sorted list between indices lower
                to upper, inclusive
    Parameters :
        sorted_list : a already sorted list
        ele : the element to be inserted
        lower : lower bound of the sublist
        upper : upper bound for the sublist
    Return value : None
    '''
    # approach : compare the element to the sorted_list[index]
    # If greater, move forward with recursion, If not, insert it at that position. 
    # If the index reaches to the end of list, perform a check, 
    # whether the existing end element is greater or smaller than the element to be inserted
    # If the existing element is smaller, insert after it
    # If greater, insert at that index.
    
    if(lower == upper):
        if(sorted_list[lower] <= ele):
            sorted_list.insert(lower+1,ele)
        else:
            sorted_list.insert(lower,ele)
        return
       
    if(sorted_list[lower] <= ele):
        insertSorted(sorted_list,ele,lower+1,upper)
    else:
        sorted_list.insert(lower,ele)
        return


sorted_list=[1,3,5,7]
print("original list     :",sorted_list)
print("")


sorted_list=[1,3,5,7]
# Test case 1
ele=9
lower=0
upper=0
print("original list     :",sorted_list)
print("Inserting element :",ele)
print("Between index     :",lower,"to",upper)
insertSorted(sorted_list,ele,lower,upper)
print("After insertion   :",sorted_list)
print("")

sorted_list=[1,3,5,7]
# Test case 2
ele=8
lower=0
upper=len(sorted_list)-1
print("original list     :",sorted_list)
print("Inserting element :",ele)
print("Between index     :",lower,"to",upper)
insertSorted(sorted_list,ele,lower,upper)
print("After insertion   :",sorted_list)
print("")

sorted_list=[1,3,5,7]
# Test case 3
ele=4
lower=0
upper=len(sorted_list)-2
print("original list     :",sorted_list)
print("Inserting element :",ele)
print("Between index     :",lower,"to",upper)
insertSorted(sorted_list,ele,lower,upper)
print("After insertion   :",sorted_list)
print("")


sorted_list=[1,3,5,7]
# Test case 4
ele=7
lower=0
upper=len(sorted_list)-3
print("original list     :",sorted_list)
print("Inserting element :",ele)
print("Between index     :",lower,"to",upper)
insertSorted(sorted_list,ele,lower,upper)
print("After insertion   :",sorted_list)
print("")

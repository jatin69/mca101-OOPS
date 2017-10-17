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


def insertion_sort(mylist,index=0):
    '''
    Objective : Sort the list
    Parameters :
        mylist : The list to be sorted
        index : to keep track of the already sorted part of the list.
    '''
    # approach : start from starting, if a problem element is found, delete it
    # from that index and use insertSorted() to insert it in (0 to index) in  sorted manner.

    if((index+1)==len(mylist)):
        return
    
    if(mylist[index+1]<mylist[index]):
        temp=mylist[index+1]
        del mylist[index+1]
        insertSorted(mylist,temp,0,index)

    return insertion_sort(mylist,index+1)


# Test case 1
mylist=[-2,-1,2,1,0,4,5,9,1]
print("\noriginal list is :",mylist)
insertion_sort(mylist)
print("sorted   list is :",mylist)


# Test case 2
mylist=[1,0,3,4,7,2,1,9,10,2,11,4]
print("\noriginal list is :",mylist)
insertion_sort(mylist)
print("sorted   list is :",mylist)

        

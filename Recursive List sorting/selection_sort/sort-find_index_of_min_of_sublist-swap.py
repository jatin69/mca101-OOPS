# Note : Finds the index of minimum element of the sublist from lower to upper-1
def find_index(mylist, lower, upper):
    '''
    Objective  : To find the index of minimum element of the sublist from lower to upper-1
    parameters :
        mylist : The list in which the min index is to be found
        lower  : The lower bound for the sublist in which min index is to be found
        upper  : The upper bound for the sublist in which min index is to be found
        min_index : Index of the minimum element, initially at lower

    Return value : min_index - The index of the minimum value
    '''
    # approach : compares the curent minimum element with each element of the supposed sublist,
    # If any element is even smaller than current min_ele, it becomes the new minimum.
    # The process repeats until lower bound reaches to upper bound

    def myfind(mylist, lower, upper, min_index):
        if(upper == lower):
            return min_index
    
        if mylist[lower] < mylist[min_index]:
            min_index=lower
    
        return myfind(mylist,lower+1,upper,min_index)


    return myfind(mylist, lower, upper, lower)
    

def sort_sel(mylist,index=0):
    '''
    Objective: sorting a list using the function find_index
    Parameters :
        mylist - the list to be sorted.
        index  - used to keep track of the current sorted list
    Return value : None
    '''
    # approach- find the index of min element from the unsorted list part
    # and then swap that min ele with first unsorted ele from start of list, move forward the sorted list index
    # repeat this until the list is sorted.

    if(index==len(mylist)-1):
        return
    
    if(mylist[index]<mylist[index+1]):
        sort_sel(mylist,index+1)

    else:   
        swap_index=find_index(mylist,index+1,len(mylist))

        temp=mylist[swap_index]
        mylist[swap_index]=mylist[index]
        mylist[index]=temp

        sort_sel(mylist,index+1)


mylist=[1,2,11,4,6,3]
print("original list is :",mylist)
sort_sel(mylist)
print("Sorted list is   :",mylist)

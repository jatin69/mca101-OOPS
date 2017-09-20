# Note : Finds the index of minimum element of the sublist from lower to upper
def find_index(mylist,lowerBound,upperBound):
    '''
    Objective  : To find the index of minimum element of the sublist from lower to upper
    parameters :
        mylist : The list in which the min index is to be found
        lowerBound  : The lower bound for the sublist in which min index is to be found
        upperBound  : The upper bound for the sublist in which min index is to be found
        
    Return value : min_index - The index of the minimum value
    '''

    '''
    approach :  Assume lower and upper as true list bounds, compare a[lowrer] <= a[upper],
                If true, approach from the upper end by decrementing upper, 
                else,    approach from the lower end by incrementing lower,
                at last, upper and lower meets at the index of min element, return this.

    '''

    if upperBound==lowerBound:
        return upperBound
    elif mylist[upperBound] > mylist[lowerBound]:
        return find_index(mylist,lowerBound,upperBound-1)
    else:
        return find_index(mylist,lowerBound+1,upperBound)



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
        swap_index=find_index(mylist,index+1,len(mylist)-1)

        temp=mylist[swap_index]
        mylist[swap_index]=mylist[index]
        mylist[index]=temp

        sort_sel(mylist,index+1)


mylist=[1,2,11,4,6,3]
print("original list is :",mylist)
sort_sel(mylist)
print("Sorted list is   :",mylist)

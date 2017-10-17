def bubble(mylist,high,low=0):
    '''
    Objective : To Bubble up the lightest element of the list
    Parameters : mylist - The list to be worked upon
                   high - the limit of  bubbling up
                   low - startin of bubble
    Return value : none
    '''
    if(high==low):
        return
    if( mylist[low]<mylist[low+1] ):
        mylist[low], mylist[low+1] = mylist[low+1], mylist[low]

    bubble(mylist,high,low+1)

def bubble_sort(mylist,high=None):
    '''
    Objective : To sort a list in Descending order
    Parameters : mylist - The list to be sorted
    Return value : none
    '''
    if high==0:
        return
    
    if high==None:
        high=len(mylist)-1

    bubble(mylist,high)
    return bubble_sort(mylist,high-1)

    
# test case 1
mylist=[-1,4,99,1,0]
print("original list : ",mylist)
bubble_sort(mylist)
print("sorted list   : ",mylist)


# test case 2
mylist=[0,4,9,0,1]
print("original list : ",mylist)
bubble_sort(mylist)
print("sorted list   : ",mylist)


# test case 3
mylist=[1,2,4,5,6,8,3]
print("original list : ",mylist)
bubble_sort(mylist)
print("sorted list   : ",mylist)

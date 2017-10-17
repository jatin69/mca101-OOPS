def ins_sort(mylist,index=0):
    '''
    Objective : Classic Insertion sort
    parameters :
        mylist : List to be sorted
        index  : To keep track of sorted sublist
    Return value : None
    '''
    '''
    approach : Find the anamoly index. Start copying elements from
    index to index+1, until you reach the correct place for anamoly element.
    Copy anamoly element at the correct place.
    '''
    if(index+1 == len(mylist)):
        return

    if mylist[index+1] < mylist[index]:
        ele=mylist[index+1]
        curr=index
        while curr>=0 and ele<mylist[curr]:
            mylist[curr+1]=mylist[curr]
            curr=curr-1

        mylist[curr+1]=ele
        
    return ins_sort(mylist,index+1)

    
# Test case 1
mylist=[0,4,5,1,9,-1,3,1,7,0]
print("\noriginal list is :",mylist)
ins_sort(mylist)
print("sorted   list is :",mylist)

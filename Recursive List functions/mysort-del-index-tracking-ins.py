mylist=[1,7,8,5,2]

def mysort(mylist,sort_index=0,unsort_index=1):
    '''
    Objective : Sort the List
    '''
    #print(" called with : sort_index = ",sort_index," and unsort index = ",unsort_index)
    #print(mylist)

    if((len(mylist)== unsort_index)):
       # print("returning")
        return

     
    # checking each element of sorted list
    if(mylist[sort_index] < mylist[unsort_index]):
       # print("in level 1 if")

        if(sort_index+1==unsort_index):
        #    print("in level 2 if 1")
            mysort(mylist,0,unsort_index+1)

        else:
         #   print("in level 2 else")
            mysort(mylist,sort_index+1,unsort_index)

    else:
        # swap the elements, is problematic ->> because even after swapping the shit becomes inconsistent
        # Instead of swapping, find a function to delete the element from unsorted_index and insert it at sorted_index
        #print("in level 1 else")
        #print("coming to Clear ",mylist[sort_index]," and ",mylist[unsort_index]) 
        #temp=mylist[unsort_index]
        #mylist[unsort_index]= mylist[sort_index]
        #mylist[sort_index]=temp

        ele = mylist[unsort_index]
        del mylist[unsort_index]
        mylist.insert(sort_index, ele)
        
        mysort(mylist,0,unsort_index+1)

        
print(mylist)
mysort(mylist)
print(mylist)    

def insertSorted(sorted_list,ele,index=0):
    '''
    Objective : Insert an element in the sorted list
    Parameters :
        sorted_list : a already sorted list
        ele : the element to be inserted
        index : a default parameter for holding index
    Return value : None
    '''
    # approach : compare the element to the sorted_list[index]
    # If greater, move forward with recursion
    # If not, insert it at that position
    # If the index reaches to the end of list, append the element
    
    if(index== len(sorted_list)):
        sorted_list.insert(index+1,ele)
        return
       
    if(sorted_list[index] <= ele ):
        insertSorted(sorted_list,ele,index+1)
    else:
        sorted_list.insert(index,ele)
        return


sorted_list=[1,2,4,5]
print("original list     :",sorted_list)
print("")

# Test case 1
ele=0
print("Inserting element : ",ele, sep="")
insertSorted(sorted_list,ele)
print("After insertion   :",sorted_list)
print("")

# Test case 2
ele=1
print("Inserting element : ",ele, sep="")
insertSorted(sorted_list,ele)
print("After insertion   :",sorted_list)
print("")

# Test case 3
ele=3
print("Inserting element : ",ele, sep="")
insertSorted(sorted_list,ele)
print("After insertion   :",sorted_list)
print("")

# Test case 4
ele=5
print("Inserting element : ",ele, sep="")
insertSorted(sorted_list,ele)
print("After insertion   :",sorted_list)
print("")

# Test case 5
ele=6
print("Inserting element : ",ele, sep="")
insertSorted(sorted_list,ele)
print("After insertion   :",sorted_list)
print("")

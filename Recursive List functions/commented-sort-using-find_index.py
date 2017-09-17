import math

def find_index(mylist, ia, ib, min_ele= math.inf, min_index= math.inf):
    '''
    Objective : To find the index of minimum element of the sublist from ia to ib-1
    '''

    if(ib == ia):
        return min_index
    
    if mylist[ia] < min_ele:
       # print("min ele is ",min_ele)
        min_ele=mylist[ia]
        min_index=ia

    # print("calling with ia=",ia," min ele : ",min_ele, " min_index= ",min_index)
    return find_index(mylist,ia+1,ib,min_ele,min_index)


def sort_sel(mylist,index=0):
    '''
    Objective: sorting a list
    '''
    # approach- find the index of min element from the unsorted list part
    # and then swap that min ele with first unsorted ele from start of list 

    #print("function called index is :",index)
    if(index==len(mylist)-1):
        return
    
    if(mylist[index]<mylist[index+1]):
        #print(" all ok, move forward")
        sort_sel(mylist,index+1)

    else:   
        # find the swap index
        swap_index=find_index(mylist,index+1,len(mylist))
        #print("swap index is : ",swap_index)
        # perform swapping
        temp=mylist[swap_index]
        mylist[swap_index]=mylist[index]
        mylist[index]=temp
        #print("new list after swapping is :",mylist)
        sort_sel(mylist,index+1)

mylist=[1,2,11,4,6,3]
print(mylist)
sort_sel(mylist)
print(mylist)
'''
ia=0
ib=len(mylist)-2
min_index=find_index(mylist,ia,ib)
print(min_index)
'''

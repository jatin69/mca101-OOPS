def rev(mylist,index=0):
        '''
        Objective : To reverse a list
        Parameter :
                mylist: The list to be reversed
        Return value : None
        '''
        # approach : Recursive & changes within the same list

        # if reached in middle, return
        if(index==(len(mylist)//2)):
                return

        # else swap extremes
        mylist[index],mylist[(len(mylist)-1)-index]=mylist[(len(mylist)-1)-index],mylist[index]

        # and call the function for index+1
        return rev(mylist,index+1)


# Test case 1
mylist=[1,2,3,4,5,6]
print("original list is : ",mylist)
rev(mylist)
print("Reversed list is : ",mylist)


# Test case 1
mylist=[1,2,3,4,5]
print("original list is : ",mylist)
rev(mylist)
print("Reversed list is : ",mylist)

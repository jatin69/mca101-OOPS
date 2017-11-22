def lsearch(ls,ele,index=0):
    if(index==len(ls)):
        return False

    if(ele==ls[index]):
        return True

    return lsearch(ls,ele,index+1)


mylist=[1,2,4,5]
print(lsearch(mylist,3))

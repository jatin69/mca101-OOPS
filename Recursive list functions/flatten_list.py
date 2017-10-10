def flatten_list(mylist,index=0,newlist=[]):

    if(index==len(mylist)):
        return newlist
    
    if(type(mylist[index])== list):
        newlist.extend(flatten_list(mylist[index],0,[]))
    else:
        newlist.append(mylist[index])

    return flatten_list(mylist,index+1,newlist)


mylist=[1,2,[3,4],[5,[6,7,[8]]],[],9]
print(mylist)
flat_list= flatten_list(mylist)
print(flat_list)

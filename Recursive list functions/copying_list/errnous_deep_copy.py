# [...] error
# code link : https://goo.gl/e8jGFA

def deep_copy(mylist,index=0,newlist=[]):
    '''
    print("\ncoming inside")
    print("mylis is ",mylist," and index : ",index)
    print("current newlist is :",newlist)
    '''
    if(index == len(mylist)):
        #print("reached end")
        return newlist
    
    if( type(mylist[index])==list ):
        #print("list encountered")
        newlist.append(deep_copy(mylist[index]))
    else:
        #print("just append")
        newlist.append(mylist[index])
        
    return deep_copy(mylist,index+1,newlist)


# long list
# a=[[1,0],0,1,[1, [2, [3, 4], [[[5]],6]]],3,[1,2,3]]

# short list
a=[1,[3,4],5]

print("original list is : ",a)
b=deep_copy(a)
print("copied list is   : ",b)


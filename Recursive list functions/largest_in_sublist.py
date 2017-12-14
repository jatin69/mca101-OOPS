def find_largest(ls,i=0,largest=None):

    if i == len(ls):
        return largest
    
    if isinstance(ls[i],list):
        temp = find_largest(ls[i],0,largest)
    else:
        temp = ls[i]
        if(largest==None):
            largest=ls[i]
        
    if(temp>largest):
        largest=temp
        
    return find_largest(ls,i+1,largest)


a= [1,2,[3,9],[],[2,1,3,[[]],6]]
print(find_largest(a))

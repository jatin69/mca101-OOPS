def remove_adjacent_duplicates(a,res=[],i=0,prev=None):

    if i==len(a):
        return res

    if(a[i] != prev):
        res.append(a[i])
    else:
        if res!=[] and res[-1]==a[i]:
            res.pop()
    
    return remove_adjacent_duplicates(a,res,i+1,a[i])

'''   
# Working iterative
def remove_adjacent_duplicates(a):
       res=[]
       i=0
       prev=None
       
       while i<len(a):
           if a[i] != prev:
               res.append(a[i]) 
           else:
                if res!=[] and res[-1]==a[i]:
                   res.pop()
                
           prev = a[i]
            
           i=i+1
           print(res)
       return res
'''           
            
    

a=[1,2,4,4,5,7,7,7,8,8,8,8,9,7]
# a=[1,1,1,2,4,4,5,5,5]
# a= [1,1,2,2,2,2,3,3]

print(a)
b=remove_adjacent_duplicates(a)
print(b)
print(b==[1,2,5,9,7])

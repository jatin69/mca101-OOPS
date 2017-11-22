
def merge(A,B,iA=0,iB=0,C=[]):
    '''
    Objective : To merge two sorted lists
    '''
    # reached end of list
    if( iA==len(A) and iB==len(B) ):
        return C

    # inside list case 1
    if( iA<len(A) and iB<len(B) ):
        if(A[iA]<B[iB]):
            C.append(A[iA])
            iA += 1
        else:
            C.append(B[iB])
            iB += 1

    # one list is over
    else:
        if(iA<len(A)):
            C.append(A[iA])
            iA +=1
            return merge(A,B,iA,iB)

        if(iB<len(B)):
            C.append(B[iB])
            iB +=1
            return merge(A,B,iA,iB)
        
    return merge(A,B,iA,iB,C)


l1=[1,3,5]
l2=[2,4,6]
l3=merge(l1,l2)
print(l3)

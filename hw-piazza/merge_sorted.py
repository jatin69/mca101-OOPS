'''
Author - Jatin Rohilla
Course - MCA 101 
'''


import pdb
#pdb.set_trace()

def merge(A,B,iA=0,iB=0,C=[]):
    '''
    Objective : Merge two sorted lists - efficiently
    parameters :
        A : sorted list A
        B : sorted list B
        iA : index tracker for list A
        iB : index tracker for list B
        C : the merged list
        
    '''

    # end of list A reached
    if( iA == len(A) ):
        # end of list B reached
        if( iB == len(B) ):
            # both lists ended, return the result
            return C
        # list A is ended, but B is still present
        else:
            C.append(B[iB])
            iB +=1
            return merge(A,B,iA,iB,C)

    # end of list A is not reached
    else:
        # end of list B reached
        if( iB == len(B) ):
            # list B is done, A is still not done
            C.append(A[iA])
            iA +=1
            return merge(A,B,iA,iB,C)

        # A not done as well as B not done 
        else:
            if(A[iA]<B[iB]):
                C.append(A[iA])
                iA += 1
                return merge(A,B,iA,iB,C)
            else:
                C.append(B[iB])
                iB += 1
                return merge(A,B,iA,iB,C)

l1=[1,2,5,8,9]
l2=[2,4,5,80,90]
l3=merge(l1,l2)
print(l3)

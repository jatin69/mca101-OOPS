# Note : Finds the index of minimum element of the sublist from lower to upper
def minIndex(ls,lowerBound,upperBound):
    '''
    Objective: to find the index of the minimum numbrer of the list
    Input Parameters:
        list: list to be given
        upperBound: upper bound of the list
        lowerBound: lower bound of the list
    Return Value: the index of the minimum numbrer of the list
    '''

    #Approach: using recursion
    if upperBound==lowerBound:
        return upperBound
    elif ls[upperBound] > ls[lowerBound]:
        return minIndex(ls,lowerBound,upperBound-1)
    else:
        return minIndex(ls,lowerBound+1,upperBound)

list = [6,11,5,12,9,8]

print("Minimum in the list",minIndex(list,0,3))

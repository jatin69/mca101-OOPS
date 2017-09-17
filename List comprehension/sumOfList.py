def sumTotal():
    '''
    Objective   : To find the sum of list
    User inputs : A list in which elements are space separated
    Output      : Sum of the list
    '''
    '''
    approach    : convert the user entered list to a integer list and loop through the list adding each element to sum variable.
    '''
    
    intList=[int(x) for x in input("Enter the list : ").split(' ')]
    sum=0
    for i in range(0,len(intList)):
        sum += intList[i]
    print("The sum of the list is :",sum)

sumTotal()

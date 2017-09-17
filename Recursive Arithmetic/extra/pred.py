def increment(number):
    '''
    Objective  : To increment the number
    Parameters : number which is to be incremented
    return value : the incremented value - new_number
    '''
    #approach : Add 1 to the number
    new_number=number+1
    return new_number


def mypredecessor(number,base=0):
    '''
     Objective: predecessor of a number
     Parameter:
         number: integer - whose predecessor is to be found
         base: default number 0, used as base condition
     return value: predecessor of a number
     '''
    #approach: Recursive

    if increment(base) == number:
        return base

    if(number>0):
        return mypredecessor(number,increment(base))

    else:
        return mypredecessor(number,decrement(base))
    # should not use decrement here, as decrement does x-1
    
def predecessor(number):
    '''
     Objective: predecessor of a number
     Parameter:
         number: integer - whose predecessor is to be found
     return value: predecessor of the number
     '''
    #approach: Using the function mypredecessor()

    return mypredecessor(number)

def main():
    '''
     objective: predecessor of user entered number
     input values:
         number: number entered by user whose predecessor is to be found
     output value: predecessor of user entered number
     '''
    #approach: Using predecessor function

    number = int(input("enter the first number: "))
    assert number>=0
    print("predecessor of a number: " , predecessor(number))

if __name__ == '__main__' :
    main()

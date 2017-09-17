# Making predecessor function using increment function

def increment(number):
    '''
    Objective  : To increment the number
    Parameters : number which is to be incremented
    return value : the incremented value - new_number
    '''
    #approach : Add 1 to the number
    new_number=number+1
    return new_number


def predecessor(number):
    '''
     Objective: predecessor of a number
     Parameter:
         number: integer - whose predecessor is to be found
     return value: predecessor of the number
     '''
    # THIS IS A wrapper function
    #approach: HouseKeeping - Using the local function mypredecessor(number,base)

    def mypredecessor(number,base):
        '''
         Objective: predecessor of a number
         Parameter:
             number: integer - whose predecessor is to be found
             base: default number 0, used as base condition
         return value: predecessor of a number
         '''
        # THIS IS A housekeeper 
        #approach: Recursive
    
        if number == 0:
            return None
        elif increment(base) == number:
            return base
        else:
            return mypredecessor(number,increment(base))

    return mypredecessor(number,0)

def main():
    '''
     objective: predecessor of user entered number
     input values:
         number: number entered by user whose predecessor is to be found
     output value: predecessor of user entered number
     '''
    #approach: Using predecessor function

    number = int(input("enter the number: "))
    assert number>=0
    print("predecessor of a number: " , predecessor(number))

if __name__ == '__main__' :
    main()

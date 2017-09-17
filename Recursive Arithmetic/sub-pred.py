# Difference of two numbers using predecessor function

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

def subtract(num1,num2):
    '''
    Objective: To subtract num2 from num1
    parameters :
        num1 - integer - first number
        num2 - integer - second number
    Return value : difference of two numbers
    '''
    #approach : Recursive using predecessor function
    if num2==0:
        return num1

    return subtract(predecessor(num1),predecessor(num2))


def main():
    '''
     objective: Subtract two numbers
     User Inputs :
        num1 - integer - first number
        num2 - integer - second number
    output value: difference of user entered numbers
     '''
    #approach: Using predecessor function

    num1 = int(input("enter the first number : "))
    assert num1>=0
    num2 = int(input("enter the second number: "))
    assert num2>=0

    if(num1>=num2):
        res = subtract(num1,num2)
    else:
        res = -1*subtract(num2,num1)
        
    print("Difference is : ",res)

    
if __name__ == '__main__' :
    main()

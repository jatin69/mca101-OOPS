# Division using Recursion

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

def sumOfTwoNumbers(num1,num2):
    '''
    Objective  : To find sum of two numbers
    Parameters :
        num1 - integer - first number
        num2 - integer - second number
    return value :
        total - sum of the two numbers
    '''
    #approach : Recursive - using increment function

    if(num2==0):
        return num1
    
    return sumOfTwoNumbers(increment(num1),predecessor(num2))
       
def mul(num1,num2):
    '''
    Objective  : To find product of two numbers
    Parameters :
        num1 - integer - first number
        num2 - integer - second number
    return value :
        product - product of the two numbers
    '''
    #approach : Recursive - using increment function

    if num2==0:
        return 0
    return sumOfTwoNumbers(num1,mul(num1,predecessor(num2)))

def subtract(num1,num2):
    '''
    Objective: To subtract num2 from num1, i.e. find num1-num2
    parameters :
        num1 - integer - first number
        num2 - integer - second number
    Return value : difference of two numbers
    '''
    #approach : Recursive using predecessor function
    if num2==0:
        return num1

    return subtract(predecessor(num1),predecessor(num2))


def div(dividend,divisor):
    '''
    Objective  : To find quotient when dividend is divided by divisor
    Parameters :
        dividend - integer - the number to be divided
        divisor  - integer - The number which will divide
    return value :
        quotient - the quotient of the divison is returned
    '''
    #approach : Invoking mydiv function

    def mydiv(dividend,divisor,quotient):
        '''
        Objective :
        '''
        #approach : Recursive
        
        if dividend>=divisor :
            return mydiv(subtract(dividend,divisor),divisor,increment(quotient))
        else:
            return quotient
        
    quotient=0
    return mydiv(dividend,divisor,quotient)
       
def main():
    '''
    Objective : To find sum of two numbers
    User inputs :
        dividend - integer - the number to be divided
        divisor  - integer - The number which will divide
    '''
    #approach : Call function mul(num1,num2)
    
    dividend= int(input("Enter the dividend  : "))
    divisor= int(input("Enter  the divisor   : "))
    assert(divisor>=0)
    
    quotient=div(dividend,divisor)
    print("Quotient is : ",quotient)


if __name__ == "__main__" :
    main()
    


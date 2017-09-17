# Product of two numbers using recursion 
#logic - 5*4 = 5+ (5*3)

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
       
def main():
    '''
    Objective : To find sum of two numbers
    User inputs :
        num1 - integer - first number
        num2 - integer - second number
    '''
    #approach : Call function mul(num1,num2)
    
    num1= int(input("Enter the first number  : "))
    assert(num1>=0)
    num2= int(input("Enter the second number : "))
    assert(num2>=0)
    
    if(num1>=num2):
        product = mul(num1,num2)
    else:
        product = mul(num2,num1)
        
    print("Product is : ",product)


if __name__ == "__main__" :
    main()
    


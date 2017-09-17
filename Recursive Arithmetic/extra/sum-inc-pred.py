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
        return mypredecessor(number,base-1)
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
    else:
        if(num2>0):
            return sumOfTwoNumbers(increment(num1),predecessor(num2))
        elif(num2<0):
            return sumOfTwoNumbers(predecessor(num1),increment(num2))
    
def main():
    '''
    Objective : To find sum of two numbers
    User inputs :
        num1 - integer - first number
        num2 - integer - second number
    '''
    #approach : Call function sumOfTwoNumbers(num1,num2)
    num1= int(input("Enter the first number  : "))
    num2= int(input("Enter the second number : "))
    if(abs(num1)>=abs(num2)):
        total = sumOfTwoNumbers(num1,num2)
    else:
        total = sumOfTwoNumbers(num2,num1)
    print("Sum is : ",total)


if __name__ == "__main__" :
    main()
    

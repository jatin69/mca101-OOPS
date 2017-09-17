def increment(number):
    '''
    Objective  : To increment the number
    Parameters : number which is to be incremented
    return value : the incremented value - new_number
    '''
    #approach : Add 1 to the number
    new_number=number+1
    return new_number


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
            return sumOfTwoNumbers(increment(num1),num2-1)
        elif(num2<0):
            return sumOfTwoNumbers(num1-1,increment(num2))
    
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
    

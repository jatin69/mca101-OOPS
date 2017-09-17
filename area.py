def areaRectangle(length , breadth):
    '''
        objective : to compute the area of the Rectangle
        input parameters : 
            length   : Length of Rectangle 
            breadth  : breadth of the Rectangle
        approach  : multiply length and breadth
        return value : area of Rectangle
    '''
    area=length * breadth
    return area

def areaSquare(side):
    '''
        objective : to compute the area of the Square
        input parameters : 
                side : side of square
        approach  : invoking areaRectangle with side as both parameters
        return value : area of Square
    '''
    area= areaRectangle(side,side)
    return area

def main():    
    '''
        objective : to compute the area of the Rectangle
        user inputs : 
            length : Length of Rectangle 
            breadth : breadth of the Rectangle
        approach  : to use function areaRectangle()
        return value : area of Rectangle
    '''
    length = int(input("Enter Length of Rectangle  :"))
    breadth =int(input("Enter Breadth of Rectangle : "))
    print('Length of Rectangle  : ' ,length)
    print('Breadth of Rectangle : ' ,breadth)
    print('Area of Rectangle    : ' , areaRectangle(length ,breadth))
    side=int(input("\nEnter Side of Square : "))
    print('Side of Square : ' ,side)
    print('Area of Square : ' , areaRectangle(side ,side))
    
if __name__ == '__main__':
    main()
print("End of the Program")

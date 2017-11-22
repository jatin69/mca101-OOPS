''' 
Area of a rectangle: 
https://goo.gl/5FVoMY
'''

def areaRectangle(length, breadth):
    '''
    objective : To Compute area of a rectqangle 
    input parameters :
        length : length  of rectangle
        breadth: breadth of rectangle
    approach: multiply length and breadth
    return value: area of rectangle
    '''
    area=length*breadth
    return area
    
def main():
    '''
    objective : To Compute area of a rectqangle 
    user inputs :
        length : length  of rectangle
        breadth: breadth of rectangle
    approach: use function areaRectangle(length, breadth)
    '''
    length= int(input("Enter the length : "))
    breadth= int(input("Enter the breadth : "))
    print("Length is : ",length)
    print("Breadth is : ",breadth)
    print("Area : ",areaRectangle(length, breadth))
    print('End of main')
    
if __name__ == "__main__":
    main()
    print('End of Program')

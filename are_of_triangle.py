'''
Area of a Triangle:
https://goo.gl/TC2yRf
'''


def areaTriangle(base, height):
    '''
    objective : To Compute area of a Triangle 
    input parameters :
        base : base  of Triangle
        height: height of Triangle
    approach: multiply base and height
    return value: area of Triangle
    '''
    area=0.5*base*height
    return area
    
def main():
    '''
    objective : To Compute area of a Triangle 
    user inputs :
        base : base  of Triangle
        height: height of Triangle
    approach: use function areaTriangle(base, height)
    '''
    base= int(input("Enter the base of triangle : "))
    height= int(input("Enter the height of triangle : "))
    print("Base is : ",base)
    print("Height is : ",height)
    print("Area : ",areaTriangle(base, height))
    print('End of main')
    
if __name__ == "__main__":
    main()
    print('End of Program')

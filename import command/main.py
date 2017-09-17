import sys
sys.path.append('/home/Desktop/jatin')
import area

def main():    
     '''
     objective : to compute the area of the Rectangle,square,triangle by appending another file
     user inputs :
         choice  : Taking the user choice
         length  : Length of Rectangle 
         breadth : breadth of the Rectangle
         side    : side of the square
         base    : base of the triangle
         height  : height of the triangle
    
     '''
     # approach  : Call the required function after taking the user choice

     print("\n\t **** Menu ****\n\n \
     1. area of rectangle\n \
     2. area of square\n \
     3. area of triangle\n")

     choice = int(input("Enter your choice:  "))
     print("")

     if choice == 1:
       length = int(input("Enter Length of Rectangle  :"))
       breadth =int(input("Enter Breadth of Rectangle :"))
       print('Length of Rectangle  : ' ,length)
       print('Breadth of Rectangle : ' ,breadth)
       print('Area of Rectangle    : ' ,area.areaRectangle(length ,breadth))

     elif choice == 2:
       side=int(input("Enter Side of Square : "))
       print('Side of Square : ' ,side)
       print('Area of Square : ' , area.areaSquare(side))

     elif choice == 3:
       base =   int(input("Enter base of triangle   :  "))
       height = int(input("Enter height of triangle :  "))  
       print("Area of triangle         : ",area.areaTriangle(base ,height))

     else:
          print("Invalid Option. Retry !")
       
if __name__ == '__main__':
     main()
     print("\nEnd of the Program\n")

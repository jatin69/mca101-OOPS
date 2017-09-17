import sys
sys.path.append('/home/Documents/jatin')
import trigo

def main():
    '''
    Objective   : To print the value cosine x
    User inputs :
         x - int : The value in degrees whose cosine is to be calculated
         
    '''
    #approach : Using Taylor series expansion of cosine x
    print('{:^40}'.format("Trigonometric functions"))
    
    print("\n \
          1. Sine x  \n \
          2. Cosine x \n")

    choice = int(input("Enter your choice:  "))
    print("")

    if choice == 1:
       xDegrees = int(input("Enter the angle in degrees :  "))
       print('Value of  Sine',xDegrees,'is       : ', trigo.sine(xDegrees))

    elif choice == 2:
       xDegrees = int(input("Enter the angle in degrees :  "))
       print('Value of Cosine',xDegrees,'is      : ', trigo.cosine(xDegrees))

    else:
          print("Invalid Option. Retry !")
       
if __name__ == '__main__':
     main()
     print("\nEnd of the Program\n")

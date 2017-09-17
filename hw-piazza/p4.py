def isoTriangle(S):
    '''
    objective : To print a isoceles triangle 
    approach : Using print statements
    argument : 
            S : the symbol for triangle
    '''
    print("\n\n\n")
    print("           ",S)
    print("         ",S,S,S)
    print("       ",S,S,S,S,S )
    print("     ",S,S,S,S,S,S,S )
    print("   ",S,S,S,S,S,S,S,S,S)
    print(" ",S,S,S,S,S,S,S,S,S,S,S)
    print("\n\n\n")
    print('End of Triangle')
    
def main():
    '''
    objective : To print a isoceles triangle 
    approach : Using print statements
    user inputs:
        symbol : the symbol used to display the triangle
    '''
    symbol=input("Enter the symbol : ")
    isoTriangle(symbol)
    print('End of main')
    
if __name__ == "__main__":
    main()
    print('End of Program')

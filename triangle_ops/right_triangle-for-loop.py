'''
To print a right triangle Using loops: 
https://goo.gl/PEyS9a
'''

def rtTriangle():
    '''
    objective : To print a right triangle 
    approach : Using loops
    '''
    for row in range(0,4):
        for column in range(0,row+1):
            print('*',end='')
        print('')
    print('End of Triangle')
    
def main():
    '''
    objective : To print a right triangle 
    approach : Using print statements
    '''
    rtTriangle()
    print('End of main')
    
if __name__ == "__main__":
    main()
    print('End of Program')

import matplotlib.pyplot as plt

def square(x, y):
    '''
    Objective: To plot a square
    Input Parameters: x, y - lists of x coordinates and y
    coordinates respectively
    Return Value: None
    '''
    plt.plot(x, y, 'ro--')

def main():
    '''
    Objective: To plot a pattern of squares inside squares, iteratively
    Input Parameter: None
    Return Value: None
    '''
    size = int(input('Enter size of the square: '))

    
    
    s=0
    plt.title('Square')
    plt.axis([s-1, size+1, s-1, size+1])
    plt.grid()


    if size%2 == 0:
        lines= (size//2)
    else:
        lines= (size//2)+1
    

    for i in range(lines):
        x = [s,size-i,size-i,s,s]
        y = [s,s,size-i,size-i,s]
        coord=[]
        for i in range(5):
            coord.append((x[i],y[i]))
        print(coord)
        s += 1
        square(x, y)
        
    #x = [0, size, size, 0, 0]
    #y = [0, 0, size, size, 0]
    #square(x, y)
    
    
    plt.show()

if __name__ == '__main__':
    main()

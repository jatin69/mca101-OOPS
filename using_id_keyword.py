'''
Learning to use id keyword
and memory storages
link - https://goo.gl/okdvEy
'''

def areaRectangle(length, breadth):
    '''
    objective: to compute the area of a rectangle
    input parametrs:
        length: length of rectangle
        breadth: breadth of rectangle
    approach: multiply length and breadth
    return value: area of rectangle
    '''
    area = length * breadth
    return area 
    
def main():
    '''
    objective: to compute the area of a rectangle
    user inputs:
        length: length of rectangle
        breadth: breadth of rectangle
    approach: use function area_Rectangle
    '''
    length = int(input('enetr length of rectangle '))
    breadth = int(input('enetr braedth of reactangle '))
    print('id(length) ', id(length))
    print('id(breadth) ', id(breadth))
    print('id(areaRectangle) ', id(areaRectangle))
    print('areaRectangle ', areaRectangle)
    print('length of reactangle: ', length)
    print('breadth  of reactangle: ', breadth)
    print('areaRectangle: ', areaRectangle(length, breadth))
    print('End of output')
    
if __name__ == '__main__':
    main()
print('End of progam')

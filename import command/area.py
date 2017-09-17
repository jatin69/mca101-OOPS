def areaRectangle(length, breadth):
     '''
     objective : To compute the area of the Rectangle
     Input parameters : 
        length   : Length of Rectangle 
        breadth  : breadth of the Rectangle
        return value : area of Rectangle
    '''
     #approach  : multiply length and breadth
     
     area = length * breadth
     return area
    
     
def  areaSquare(side):
     '''
      objective : to compute the area of the Square
      Input parameters : 
          side : side of square
      return value : area of Square
     '''
     #approach  : invoking areaRectangle with side as both parameters
     
     area = side * side
     return area
    
    
def areaTriangle(base,height):
     '''
     Objective : to compute the area of the Rectangle
     Input parameters : 
       length   : Length of Rectangle 
       breadth  : breadth of the Rectangle
     return value : area of Rectangle
    '''
     #approach  : multiply length and breadth
     
     area = 0.5 * base * height
     return area


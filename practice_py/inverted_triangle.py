def ile(numberRows):
 '''
   Objective : To print an inverted triangle.
   Input Parameters :
   numberRows : integer-Number of rows inputted by user.
   Return value : none
 '''
 #Approach : Use of 'while' loop to print the triangle.
 numberSpaces=0
 numberStars=2*numberRows-1
 while numberStars>0:
  print(' '*numberSpaces,'*'*numberStars,sep="")
  numberStars-=2
  numberSpaces+=1

ile(3)

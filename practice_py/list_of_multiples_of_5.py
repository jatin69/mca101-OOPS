n=3

# first 5 multiples of ith element
b= [ [1*i,2*i,3*i,4*i,5*i]  for i in range(1,n+1) ]
print(b)


# i mulitples of ith element
c= [ [j*i for j in range(1,i+1)] for i in range(1,n+1)  ]
print(c)

a=[2,2,3,1,1]

b=[ sum(a[:i+1]) for i,j in enumerate(a) ]

print(b)

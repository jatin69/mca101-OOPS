'''
changes to both lists
that means, they point to same object
once and then thrice
'''
'''
a = [1,2,3]
b = ([a]*3)
print(a)
print(b)

# same effect
# a[0]=11
b[0][0] = 9
print(a)
print(b)
#'''

'''
a = [1,2,3]
b = (a,)
print(a)
print(b) 
#'''


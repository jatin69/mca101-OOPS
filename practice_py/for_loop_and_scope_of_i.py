'''
This proves that loops in python works differently.
And stops before violating the condition.
Stops by warning sign, does not cross the railing like c++
'''

# test case 1, scope test
i=2
print("\nGlobal i is : ",i)
for i in range(0,5):
    print("In  loop i  : ",i)
print("Out loop i  : ",i)


# test case 2, variable range
i=2
print("\nGlobal i is : ",i)
for i in range(i,5):
    print("In  loop i  : ",i)
print("Out loop i  : ",i)


# test case 3, skips increment
i=2
print("\nGlobal i is : ",i)
for i in range(0,10,3):
    print("In  loop i  : ",i)
print("Out loop i  : ",i)

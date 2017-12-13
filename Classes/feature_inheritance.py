# pre requisite : accessing_self_class.py

'''
The Goal is to create a Object counting class.
'''

'''
Point of focus -
When there is a possibility that subclasses may be made.
Always use,
self.__class__.count +=1
to access the current class, instead of 
A.count +=1

As when the property descends down to subclasses.
The absolute class naming will mess up things.
'''

'''
Proof of Concept
'''

print("\n\n ** Use of __class__ attribute ** ")
'''
This is class A.
It has a special property of counting objects
'''
class A:
    count=0

    def __init__(self):
        # increment count of the calling class
        self.__class__.count +=1
        print("creating A object")

a= A()
print(A.count)
print(a.count)

'''
I created a class B, in the hope that
B will inherit this special property.
'''
class B(A):
    '''
    Need to initialise count=0 again,
    to provide this class a fresh object counter,
    or otherwise, it would have started counting
    from A's count value (from that instant of time when the class B got inherited)
    '''
    
    count=0
    pass

'''
Note that,
B inherits the function __init__()
Thus inherits the print("creating A object") statement.
So when B() is created, print executes as usual.
Note that, count is incremented of the calling class, i.e. B()
count is incremented only of B. As it is now B's property
'''
print("creating B object")
b=B()
print(A.count)
print(a.count)
print(B.count)
print(b.count)

'''
More test cases to verify the independence of properties.
'''
A()
print(A.count)
print(a.count)
print(B.count)
print(b.count)

print("creating B object")
B()
print("creating B object")
B()
print(A.count)
print(a.count)
print(B.count)
print(b.count)


'''
All the above happened as expected.
Now let us see what could have gone wrong.
if we used absolute class namings.
'''

'''
But instead, it kept on increasing A.count.
Causing unexpected linking. 
'''



print("\n\n ** Absolute class name ** ")
'''
This is class A.
It has a special property of counting objects
'''
class A:
    count=0

    def __init__(self):
        # increment count of A class
        A.count +=1
        print("creating A object")

a= A()
print(A.count)
print(a.count)

'''
I created a class B, in the hope that
B will inherit this special property.
'''
class B(A):
    '''
    Need to initialise count=0 again,
    to provide this class a fresh object counter,
    or otherwise, it would have started counting
    from A's count value (from that instant of time when the class B got inherited)
    '''
    count=0
    pass

'''
Note that,
B inherits the function __init__()
Thus inherits the print("creating A object") statement.
So when B() is created, print executes as usual.
Note that, count is incremented of the calling class, i.e. B()
count is incremented only of B. As it is now B's property
'''
print("creating B object")
b=B()
print(A.count)
print(a.count)
print(B.count)
print(b.count)

'''
More test cases to verify the independence of properties.
'''
A()
print(A.count)
print(a.count)
print(B.count)
print(b.count)

print("creating B object")
B()
print("creating B object")
B()
print(A.count)
print(a.count)
print(B.count)
print(b.count)


'''
The problem is pretty clear.

Even more blunders would happen,
if we didn't initialise the count=0 in class B
That way,
we could have hardly detected the bug, as the numbers seemed okay.
'''

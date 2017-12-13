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
Preferred way when possibility of sub classes
'''
class A:
    count=0

    def __init__(self):
        # increment count of the calling class
        self.__class__.count +=1
        print("creating A object")


'''
This works fine for non inheritance cases,
but still a dangerous practice, as it hampers the code extension possibility.
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

'''
Class attributes are modifiable only by Class, not by its instance.
'''

class A:
    count=0
    
    def __init__(self):
        self.__class__.count +=1
        print("object created.")


a=A()
b=A()

'''
Instances have only read access to class attributes
'''
print("\n ** Instances have only read access to class attributes ** ")
print(A.count)

# a does not have a 'count' of its own
print(a.count)
print(a.__dict__)

print(b.count)
print(b.__dict__)


'''
Class have supreme rights over class attributes.
One change reflects back to all objects
'''
print("\n ** Class have supreme rights over class attributes ** ")
A.count=5
print(A.count)

# a still does not have a 'count' of its own
print(a.count)
print(a.__dict__)

print(b.count)
print(b.__dict__)


'''
When we try to modify the class attribute with instance,
changes are made only in that instance.
No changes happens in original Class attribute.
What really happens is, it searches for 'count' in instance for writing,
but can't find, so it creates a new count.
The same can be verified by __dict__
'''
print("\n ** Objects cant modify class attributes ** ")
a.count=10
print(A.count)

# a now have a 'count' of its own
print(a.count)
print(a.__dict__)

print(b.count)
print(b.__dict__)


'''
That means, if we try to write access a non-existent variable,
it will get created, for that instance.
'''
print("\n ** writing non-existent variables ** ")
a.name="Jatin"
print(a.__dict__)


'''
WHAT comes ahead is even more interesting.

We knew that class have the supreme power, and changes reflect back to all objects.
What really happens is, it just modifies its class attribute.
It does not modify any instance variable.

That means,
if an object tried to modify a class attribute,
he won't find it, thus, create it for that instance,
thus the supreme power reflection of class will no longer hold true for that instance,
as the variable is now its own.
'''
print("\n ** The Side effect story ** ")
A.count=15
print(A.count)
# a now have a 'count' of its own
print(a.count)
print(a.__dict__)

print(b.count)
print(b.__dict__)

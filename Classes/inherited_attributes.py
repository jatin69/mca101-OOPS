# pre-requisite: The tale of class attributes

class Emp:
    count=1
    pass

john = Emp()
print(john.count)
print(john.__dict__)

# changes only occur in that instance
john.name="name"
john.count=5
print(john.count)
print(john.__dict__)

# No changes in class attribute
print(Emp.count)

print("\n")

'''
we know that each class is inherited from the object class
so the large number of elements we see are actually inherited from
object class. This is similar to java.
But still a few are its own
'''
print("\n ** all the members of the class Emp ** ")
print(*dir(Emp),sep="\n")
print("\n ** non inherited (atleast from object class ) members of the class Emp ** ")
print(set(dir(Emp))-set(dir(object)),sep="\n")


'''
same applies to objects
'''
print("\n ** all the members of the object john ** ")
print(*dir(john),sep="\n")
print("\n ** non inherited (atleast from object class ) members of the object john ** ")
print(set(dir(john))-set(dir(object)),sep="\n")



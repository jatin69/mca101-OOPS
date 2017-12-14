class Person:
    count=0

    def __init__(self,name,rollno):
        '''
        dont call it Constructor, we have __new__ for that
        It is initialiser
        '''
        self.name=name
        self.rollno=rollno
        self.const="jatin rohilla"
        Person.count += 1

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def getCount(self):
        return Person.count

    def __str__(self):
        return 'Name is '+str(self.name)+' and rollno : '+str(self.rollno)+\
        " and constant is :"+self.const

    def __del__(self):
        ''' destructor '''
        Person.count -=1

    
p1=Person("Jatin",15)
p2=Person("Jatin","ok")

print(p1)
print(p2)

# del p1

'''
>> type(Person)
<class 'type'>
>>> type(type)
<class 'type'>


'''

if "Ni!":
    print("we say hello")
else:
    print("stop")

if 0:
    print("if")
else:
    print("else")

'''
total, limit=0,1000

for i in range(1,limit,7):
    print("i is : ",i)
    for j in range(limit):
        total +=1
        
print(total)
'''

'''
class A(object):
    def __init__(self):
        self.a=1

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a=2
        self.b=3



class C(object):
    def __init__(self):
        self.a=4
        self.c=5

class D(C,B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d=6

obj=D()
print(obj.a)
print(obj.b)
print(obj.c)
print(obj.d)
'''

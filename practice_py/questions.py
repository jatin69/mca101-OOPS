'''
# q1
class Vehicle:
    pass

class Truck(Vehicle):
    pass


print(isinstance(Vehicle(), Vehicle))
print(type(Vehicle()) == Vehicle)
print(isinstance(Truck(), Vehicle))
print(type(Truck()) == Vehicle)
#'''


'''
# q2
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon)
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham)
#'''





'''
d1={
    'a':100,
    'b':200,
    'c':300
    }


d2={
    'a':300,
    'b':200,
    'd':400
    }

all_keys = set(list(d1.keys()) + list(d2.keys()))

d3={}

for key in all_keys:
    d3[key]=d1.get(key,0)+d2.get(key,0)

print(d3)
#'''




'''
unique=[]

l=[1,2,3,2,5,1,1]
print(l)
for ele in l:
    if ele not in unique:
        unique.append(ele)

print(unique)
'''


'''
sample="Note that apoorva is not that poor"
'''

'''
q3
given a list 
a=[1,2,3]

Tell Difference between
a=[4,5,6]

and

a[:]=[4,5,6]
'''
'''

'''
'''
# output
q4
spam = 'SpamSpamEggsampSampS'
print(spam.strip('ampS'))
print(spam.strip('Spam'))
'''


'''
# output
spam=[1,3,2,5,4,7,6,9,8,10]
print(spam[int(int('3' * 2) // 11)] )
#'''

'''
a = [1,2]
b = (1,2)


# diff between
a= (42)
b= (42,)

a = True
b = False
c = False
 
if a or b and c:
    print "python"
else:
    print "mca101"

'''
'''
def compute(d,n):
    sum=0
    for k in range(1,n+1):
        temp=0
        for i in range(k):
            temp += (d * (10**i))
        sum +=temp
    print(sum)

compute(9,3)
'''
#'''

'''
def compute(d,n):
    sum=0
    for k in range(1,n+1):
        temp= int(str(d)*k)
        sum +=temp
    print(sum)

print(compute(9,3))
# computing 999 + 99 + 9

'''

paragraph = 'Good \
             morning india'


'''
# -------------------------------

def func(bar=[]):
    bar.append('xyz')
    return bar

print(func())
print(func())
print(func())

# --------------------------------

def func(bar=None):
    bar= []
    bar.append('xyz')
    return bar

print(func())
print(func())
print(func())

#'''

'''
#-------------------------------
ls=[1,2,3]

def func():
    ls.append(4)

func()
print(ls)

#----------------
ls=[1,2,3]

def func():
    ls += [4]

func()
print(ls)

#-------------------------------
#'''

'''
# no of 1's in a decimal number
a=43
num="{0:b}".format(a)
print(num)
count=0
for i in str(num):
    if i is '1':
        count +=1
print(count)
#'''







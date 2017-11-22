'''
link - https://softwareengineering.stackexchange.com/a/194280
'''
'''	
I think the real answer is:
Python was written as a procedural language and
only adopted functional aspects after-the-fact.

What you're looking for is for parameter defaulting to be done as a closure,
and closures in Python are really only half-baked. 
'''
a = []
for i in range(3):
    a.append(lambda: i)

# f is a function
print([ f() for f in a ])


'''
Expected - [0,1,2]
Actual - [2,2,2]
'''


'''
There are quite a lot of things that I'd like if
Python had the ability to wrap parameter defaulting in closures.
For example:

def foo(a, b=a.b):
    ...
Would be extremely handy, but "a" isn't in scope at function definition time,
so you can't do that and instead have to do the clunky:

def foo(a, b=None):
    if b is None:
        b = a.b
        
Which is almost the same thing... almost.
'''

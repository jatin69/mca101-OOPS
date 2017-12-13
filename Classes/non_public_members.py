'''
Non-public attributes are those that are not intended to be used by third parties.
We don't use the term "private" here, since no attribute is really private in Python,
as they are still accessible.

If your class is intended to be subclassed,
and you have attributes that you do not want subclasses to use,
consider naming them with double leading underscores and
no trailing underscores.

This invokes Python's name mangling algorithm,
where the name of the class is mangled into the attribute name. This helps avoid attribute name collisions should subclasses inadvertently contain attributes with the same name.
'''

class Bar(object):
    count=2
    def __init__(self):
        self.__zap = 1
        self.a=2

a = Bar()
# print(a.__zap)
'''
The above lines give error.
AttributeError: 'Bar' object has no attribute '__zap'
'''

# check this out, the attribute exists but with mangled name
print(a.__dict__)

# Is accessible with this, so not really private, but non-public enough
print(a._Bar__zap)


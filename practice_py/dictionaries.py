d1= {
    (1,2) : 1,
    (1,2) : 2
    }

d2= {
    1 : "hi",
    2 : "jatin"
    }

d3= {
    '1' : "hi",
    '2' : "jatin"
    }

# frozen sets are also hashable
# dictionary keys can be any data type as long as it is hashable.

'''
List of immutable types:
int, float, decimal, complex, bool, string, tuple, range, frozenset, bytes

List of mutable types:
list, dict, set, bytearray, user-defined classes
'''

'''
An object is hashable if
it has a hash value which never changes during its lifetime (it needs a __hash__() method),
and can be compared to other objects (it needs an __eq__() or __cmp__() method).

Hashable objects which compare equal must have the same hash value.
Hashability makes an object usable as a dictionary key and a set member,
because these data structures use the hash value internally.

All of Python’s immutable built-in objects are hashable,
while no mutable containers (such as lists or dictionaries) are.

Objects which are instances of user-defined classes are hashable by default;
they all compare unequal, and their hash value is their id().
'''



d= {
    'a' : "hi",
    'b' : "jatin"
    }

print(d.items())

# just a view of the original dict. Not independent of dict.
print(d.keys())
print(d.values())


print('a' in d.keys())

# works as d.keys()
print('a' in d)

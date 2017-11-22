''' Golden Rules

There are four rules to tell whether a variable is in a
local scope or global scope:

1. If a variable is being used in the global scope
(that is, outside of all functions), then it is always a global variable.

2. If there is a global statement for that variable in a function,
it is a global variable.

3. Otherwise, if the variable is used in an assignment statement
in the function, it is a local variable.

4. But if the variable is not used in an assignment statement,
it is a global variable.

'''

def redo():
    print(num)


'''
    To show that :
    In a function, a variable will either always be global or always be local.
    There’s no way that the code in a function
    can use a local variable named eggs and then later
    in that same function use the global eggs variable.
'''
def test():
    '''
    If any attempt are make to access the global variable in a function
    where later on you will use local or global, it'll be referencing error
    '''

    '''
    Syntax error :
    print(num)
    global num
    as well as this,
    num=11
    global num
    
    Runtime error :
    print(num)
    UnboundLocalError: local variable 'num' referenced before assignment

    Conclusion :
    No referencing can be made prior to using global (if used)
    No referencing can be made prior to declaring global (if declared)
    '''
    global num
    num=11
    print(num)
    redo()

num=10
test()

    


'''
def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is a local

def ham():
    print(eggs) # this is the global


# this is the global
eggs = 42 

# changes made to global
spam()
print(eggs)


# changes made to local
bacon()
print(eggs)

# use global as no assignment made
ham()
#'''

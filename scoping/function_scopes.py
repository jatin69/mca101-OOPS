def f():
    a=32
    print('global f')

def g():
    a=53
    global f
    print('id(f): ',id(f))
    def f():
        a=3
        print('inner f')
    print('id(f): ',id(f))
    f()

def h():
    print('inside h: id(f):',id(f))

def main():
    print(id(f))
    f()
    g()
    g()
    h()

if __name__ == '__main__':
    main()

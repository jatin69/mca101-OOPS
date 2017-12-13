# computing 999 + 99 + 9

def itr_compute(d,n):
    sum=0
    for k in range(1,n+1):
        temp= int(str(d)*k)
        sum +=temp
    return sum

print(itr_compute(9,3))


def rec_compute(d,n):
    if n==1:
        return d
    return int(str(d)*n) + rec_compute(d,n-1)

print(rec_compute(9,3))


def rec2_compute(d,n):
    if n==1:
        return d

    i=n-1
    temp=0
    while i>=0:
        temp += d*(10**i)
        i=i-1
    
    return temp + rec2_compute(d,n-1)

print(rec2_compute(9,3))

# 999 + 99 + 9
# (900 + 90 + 9 ) + (90 + 9 ) + (9)

def rec3_compute(d,n,i=None):
    if i==None:
        i=n-1

    if i==-1:
        n=n-1
        i=n-1

    if n==1:
        return d
    
    return d*(10**i) + rec3_compute(d,n,i-1)

print(rec3_compute(9,3))




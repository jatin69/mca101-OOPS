'''
Over writes value with 0

i=5
print("Global i :",i,end="\n\n")
for i in range(i):
    print("Looped i :",i)

print("\nGlobal i :",i)
'''


'''
Does not go inside loop

i=5
print("Global i :",i,end="\n\n")
for i in range(i,5):
    print("Looped i :",i)

print("\nGlobal i :",i)
'''

'''
Does not go inside loop
i=5
print("Global i :",i,end="\n\n")
for i in range(i,i):
    print("Looped i :",i)

print("\nGlobal i :",i)
'''

i=5
print("Global i :",i,end="\n\n")
for j in range(i):
    print("Looped i :",j)

print("\nGlobal i :",i)

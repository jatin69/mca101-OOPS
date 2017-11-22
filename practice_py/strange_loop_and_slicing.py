
# don't iterate a list while modifying it
my=[1,2,3,4,5,6,7,8,9]

print(my)
# even slicing isn't safe in this case. causes error as it retains diff list
for i in my[:]:
    if(my[i]%2==0):
        my.remove(my[i])
        my.pop()
print(my)


my=[1,2,3,4,5,6,7,8,9]

print(my)
for i in my:
    if(i%2==0):
        my.remove(i)
        my.pop()
print(my)




# do not iterate a list while modifying it
my=[1,2,3,4,5,6,7,8,9]

print(my)
for i in my[:]:
    if(i%2==0):
        my.remove(i)
        my.pop()
print(my)

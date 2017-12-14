def group_by_owners(d1):

    d2={}
    
    for key in list(d1.keys()):
        d2[d1[key]] = d2.get(d1[key],[]) + [key]

    return d2


d1= {
        'Input.txt':'Randy',
        'Code.py':'Stan',
        'Output.txt':'Randy'
    }

print(d1)
d2= group_by_owners(d1)
print(d2)



'''
# first draft

def group_by_owners(d1):
    d2={}
    for key in list(d1.keys()):
        if d1[key] in list(d2.keys()):
            d2[d1[key]] += [key]
        else:
            d2[d1[key]] = [key]
        
    return d2
'''

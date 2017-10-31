
#4.10.1. Dictionary view objects
'''
d = {'k1':'val1','k2':'val2','k3':{'k4':{'k5':'100500'}}}

if 'k4' in d:
    print('KEY is in dict')
else:
    print('KEY is not in dict')

print(d['k3'])


#dictionary view
keys = d.keys()
values = d.values()
itm = d.items()

for x in iter(d):
    print('x=',x,'type(x)',type(x))

for y in keys:
    print('y=',y,'type(y)',type(y))

print(type(keys))
print(type(values))
print(type(itm))
#<class 'dict_keys'>
#<class 'dict_values'>
#<class 'dict_items'>

for t in itm:
    print("type ",type(t)," val=",t)

if 'k1' in keys:
    print('k1 is key of dict')

for val in values:
    print(val)

print(len(keys))
print(len(values))

del d['k2']

print(len(keys))
print(len(values))

nd = d.copy()

print(id(d))
print(id(nd))

print(d)
print(nd)

print('-----------------')
del nd['k3']

print(d)
print(nd)

print('-----------------')
c = d.get('k3')
print(type(c))
print(c)

print('=========================')
#get element and remove it from dict
r = {'k1':'val1','k2':'val2','k3':'val3'}
for x in range(len(r.keys())):
    print(x)
    z=r.popitem()
    print(z)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print('r=',r)
'''

r2 = {'k1':1,'k2':2,'k3':3}
print(r2)
r2.update({'k1':100}) #!!!!!!!!!!!!!!!
print(r2)

for x in r2.keys():
    r2.update({x: r2.get(x)+1000})

print(r2)

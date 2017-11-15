from operator import itemgetter
#https://stackoverflow.com/questions/25050311/extract-first-item-of-each-sublist-in-python




'''
def multiply(x):
    return (x*x)

def add(x):
    return (x+x)

def mult3(x):
    return x*2

def getv(x):
    return x

funcs = [getv, multiply, add, mult3]
for i in range(5):
    #print(i)
    value = list(map(lambda x: x(i), funcs))
    print(value)
'''

# i =0..4


#print(lc)

'''
l_grbs = [['164', 1], ['971', 1], ['054', 1], ['056', 1], ['783', 1]]

print(list(map(itemgetter(0), l_grbs)))
print(list(map(itemgetter(0), l_grbs)).index('056'))

print([item[0] for item in l])

list(map(itemgetter(0), my_list))

def grbs_in_list(lst,sgrbs):
    try:
        if sgrbs in l_grbs[:][:][0]
    except IndexError as ie:
        return False
'''
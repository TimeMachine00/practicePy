'''position'''
'''''
def person(age, name):

    print(name)
    print(age)
person('fox', 23)
'''
'''keyword'''
''''
def person(age, name):

    print(name)
    print(age-9)
person(name='fox', age=23)
'''

'''default'''
'''''
def person(name, age=18):

    print(name)
    print(age)
person('fox')
'''

'''variable length'''
'''''
def add(x,*y):
    c=x
    for i in y:
        c=c+i
    print(c)
add(1,2,3,4,5)
'''

'''key word variable length'''

def person(name, **data):
    print(name)
    for i, j, in data.items():
        print(i,j)
person('fox',age=23, city='bangalore', mobile=7778866)
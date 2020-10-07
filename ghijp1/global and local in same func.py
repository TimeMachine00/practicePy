a=10
'''' global a'''
def hi():

    a=9
    x=globals()['a']

    print('in func ',a)


    globals()['a'] = 15
hi()

print ('out fuct ', a)
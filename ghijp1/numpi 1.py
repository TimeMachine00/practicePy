from numpy import *
'''''
arr=array([1,2,2,4],float)
print(arr)
'''''

a1=array([2,3,4,5])
'''''
a2=a1+5

a2=array([2,3,4,5])
print(concatenate([a1,a2]))

print(sin(a1))
'''

'''''
a2=a1.view()
'''
a2=a1.copy()
a1[1]=9
print(a1,a2)
print(id(a1))
print(id(a2))

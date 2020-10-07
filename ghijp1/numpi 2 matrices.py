from numpy import *
'''''
a1=array([ [2,3,4,5,6,7],

            [3,4,5,6,7,8]

         ])
a2=a1.flatten()
a3=a2.reshape(3,4)
print(a3)
'''
m1=matrix('1 2 3; 1 2 3;1 2 3')
m2=matrix('1 2 3; 1 2 3;1 2 3')
m3=m1*m2
print(m3.diagonal())

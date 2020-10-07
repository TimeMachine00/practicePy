from array import *
vals= array('i',[2,3,4,5,6])
newvals=array(vals.typecode, (a*a for a in vals))
'''
for e in newvals:
    print(e)
    '''
i= 0
while i<len(newvals):
    print(newvals[i])
    i+=1
from array import  *
vals=array('i',[])
n = int(input('enter the length of a array'))
for i in range(n):
    x=int(input('enter next value'))
    vals.append(x)


print(vals)
search=int(input('enter val for search'))
k=0
for e in vals:
    if e==search:
        print(k)
        break
    k+=1
print(vals.index(search))
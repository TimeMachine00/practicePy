from functools import reduce

def fil(n):

        return n%2==0
def update(n):
    return n*n

def addall(a,b):
    return (a+b)
x=[1,2,3,4,5,6,7,8,9,10]
evens=list(filter(fil, x))
print(evens)


doubles=list(map(update, evens))
print(doubles)

sum=reduce(addall, doubles)
print(sum)



evens=list(filter(lambda a: a%2==0, x))
print(evens)
doubles=list(map(lambda a: a*a, evens))
print(doubles)

sum=reduce(lambda a,b:a+b, doubles)
print(sum)

'''''
x=[3,3,4,6,7,8,9,22,66,4,7]
for i in x:
    if i%5==0:
        print(i)
        break
else:
    print('not found')
'''''
x=int(input('hey user enter number'))
for i in range(2,x):
    if x%i==0:
        print("not a prime")
        break
else:
    print('awsome it is prime')
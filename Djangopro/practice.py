# def add(a,b):
#     c=a+b
#     d=a-b
#     return c, d
#
# a=add(0,9)
# for i in a:
#     print(i)

# def add(a,b):
#     print(id(a))
#     print(id(b))
#     a=2
#     b=3
#     print(id(a))
#     print(id(b))
#     c=a+b
#     print(c)
#
# a=12
# print(id(a))
# b=12
# print(id (b))
# add(a,b)



# def update(x):
#     print(id(x))
#     # x[0]=7
#     print(id (x))
#     print(x)
# a=[2,3,4,5,6]
# print(id(a))
# update(a)
# print(a)

# def user(name, **b):
#     print(name
#           )
#
#     for i,j in b.items():
#         print(i,j)
#
#
# z=user('huss',age=12,place='knl')
#
# print(z)

# a= 12
# def ace(a):
#
#
#
#     x=globals()['a']
#     globals()['a']=16
#
#     print(a)
#
# ace(a)
# print(a)

# def fib(n):
#     a=0
#     b=1
#     if n==1:
#         print(a+b)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c=a+b
#             a=b
#             b=c
#             print(c)
#
# n = int(input("hey baby eneter your limit to find fibnochi series"))
# fib(n)
# def fact(n):
#     if n==0:
#         print(1)
#     else:
#         f=1
#         for i in range(1,n+1):
#             f=f*i
#         return f
# n=int(input("eneter n"))
# z=fact(n)
# print(z)

# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
#
# n=int(input('enter n'))
# z=fact(n)
# print(z)

# c=lambda a,b:a+b
# z=c(2,3)
# print(z)
# class add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#         self.sub=self.Sub
#     def sum(self):
#         print(self.a+self.b)
#     class Sub:
#         def __init__(self,c,d):
#             self.c=c
#             self.d=d
#         def minus(self):
#             print(self.c-self.d)
#
#
# k=add(2,3)
# l=add(20,3)
# k.sum()
# l.sum()
# g=add.Sub(20,30)
# g.minus()

# class add:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def sum(self):
#
#         print(self.a+self.b)
#
# class add1:
#     def sum1(self,z):
#         z.sum()
#
#
# k=add(20,30)
#
#
# l=add1()
# l.sum1(k)


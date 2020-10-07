class Sum:
    def add(self,a=None, b= None ,c=None):
        d=0
        if a!=None and b!=None and c!=None:
            d=a+b+c
        elif a!=None and b!=None:
            d=a+b
        else:
            d=a

        return d
a1=Sum()
result=a1.add()
print(result)

''''class A:
    def phone(self):
        print("hi son")
class B(A):
    def phone(self):
        print("hi father")


a=B()
a.phone()'''''

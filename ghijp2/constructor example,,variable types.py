class jooli:
    color='white'
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def joolidetails(self):
        pass
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


j1=jooli('reshma',40)


j2=jooli('kavya', 40)
j2.age=20
jooli.color='black'
if j1.compare(j2):
    print('they are equal')
else:
    print('not equal')
print(j1.age,j2.age, j1.color,j2.color)





class stu:
    name='vjit'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    @classmethod
    def school(cls):
        return cls.name
    @staticmethod
    def info():
        print("this school is good")
s1=stu(70,60,90)
s2=stu(38,90,77)
print(s1.avg())
print(s2.avg())
print(stu.school())
stu.info()

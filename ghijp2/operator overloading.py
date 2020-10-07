class Stu:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Stu(m1,m2)
        return s3
    def __str__(self):
        return  '{} {}'.format(self.m1,self.m2)


s1=Stu(20,50)
s2=Stu(70,50)
s3=s1+s2
print(s3.m1)
print(s1)


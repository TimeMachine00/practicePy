class A:
    def __init__(self):
        print("in it in A")
    def feture1(self):
        print("feature A-1 is working")
    '''def feture2(self):
        print("feture 2 is working")'''

class B():
    def __init__(self):
        print("in it in B")
        super().__init__()
    def feture1(self):
        print("feature B-! is working")

    def feture4(self):
        print("feture 4 is working")
class C(A,B):
    def __init__(self):
        print("in it in c")
        super().__init__()
        super().feture4()
    def feture5(self):
        print("feature 5 is working")



a1=C()
a1.feture1()





class emp:
    company='dxc'
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.lapi=self.lapi()
        self.company=self.company
    def empdetails(self):
        print((self.name,self.id,self.company))
        self.lapi.lapidetails()
    class lapi:
        def __init__(self):
            self.brand='hp'
            self.ram=8
            self.processor='i7 intel'
        def lapidetails(self):
            print(self.brand,self.ram,self.processor)


e1=emp('hussain' ,11)
e2=emp('ravi',12)
e1.empdetails()
e2.empdetails()


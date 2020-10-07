class qcomputer:
    def __init__(self, cpu, ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print('config is ', self.cpu, self.ram)

qcom1=qcomputer('i5',16)
qcom2=qcomputer('ryzen',8)

qcom1.config()
qcom2.config()


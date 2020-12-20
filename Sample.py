class computer:

    def __init__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
    def config(self):
        print("config=" , self.cpu, self.ram)


com1 =computer('ss',12)
com1.config()
computer.config(com1)
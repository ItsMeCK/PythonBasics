class Computer:
    def __init__(self, cpu, ram):
        print("In Init")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config", self.cpu, self.ram)

comp1 = Computer('I5', '16gb')
comp1.config()
Computer.config(comp1)
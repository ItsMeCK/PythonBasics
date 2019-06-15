class Computer:
    manufactur = 'Sony'

    def __init__(self, cpu, ram):
        print("In Init")
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config", self.cpu, self.ram)

    @classmethod
    def get_manufacturer(self):
        print(self.manufactur)

comp1 = Computer('I5', '16gb')
comp1.config()
Computer.get_manufacturer()
Computer.config(comp1)
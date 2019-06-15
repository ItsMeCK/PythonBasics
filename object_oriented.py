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


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.lap = self.Laptop()
    def show(self):
        print(self.name)
        print(self.age)
        self.lap.show()

    class Laptop:
        def __init__(self):
            self.memory = '15gb'
        def show(self):
            print('Laptop')

s1 = Student('Chandrakant', 25)
s1.show()


#inheritance
print('Inheritance')
class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A):
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")


b = B()
b.feature1()

#Muliple inheritance
print('Inheritance')
class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B:
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A,B):
    def feature5(self):
        print("Feature 3 is working")

    def feature6(self):
        print("Feature 4 is working")


c = C()
c.feature3()

#constructor in inheritance
print("constructor in inheritance")

class A:
    def __init__(self):
        print('In A Init')
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B(A):
    def __init__(self):
        super().__init__()
        print('In B Init')
    def feature3(self):
        print("Feature 3 is working")

    def feature4(self):
        print("Feature 4 is working")



c = B()
c.feature3()


#Muliple inheritance - Method Resolution - Left to right
print('Inheritance')
class A:
    def feature1(self):
        print("Feature A1 is working")

    def feature2(self):
        print("Feature 2 is working")

class B:
    def feature1(self):
        print("Feature B1 is working")

    def feature4(self):
        print("Feature 4 is working")

class C(A,B):
    def feature5(self):
        print("Feature 3 is working")

    def feature6(self):
        print("Feature 4 is working")


c = C()
c.feature1()

#Duck Typing
class PyCharm:
    def execute(self):
        print('Compiling')
        print('running')

class MyIde:
    def execute(self):
        print('Compiling')
        print('running')
        print('Debug')
        print('Smart')

class Laptop:
    def code(self, ide):
        ide.execute()

print('ide is duck typing. What it cares is object has execute method. It doesnt care about its type/class')

ide = PyCharm()
lap = Laptop()
lap.code(ide)


ide = MyIde()
lap = Laptop()
lap.code(ide)


#operator overloading
print('operator overloading')



class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

s1 = Student(10, 20)
s2 = Student(20, 10)
s3 = s1 + s2
print(s3.m1)

#Method overloading
print('Method overloading')

class A:
    def show(self):
        print('In A')

class B(A):
    def show(self):
        print('In B')

b = B()
b.show()




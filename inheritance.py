class A:

    def __init__(self):
        print("In A init")

    def show1(self):
        print("A show1")

class B(A):

    def __init__(self):
        print("In B init")

    def show1(self):
        super().show1()
        print("B show1")

a = A()
# a.show1()
b = B()
b.show1()
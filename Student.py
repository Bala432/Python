class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + " has age "+ str(self.age)

    def run(self):
        return "running"


s1 = Student('A',22)
s2 = Student('B',33)

print(s1)
print(s2)

    
class Student:
    subjects = 5
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name+" having age "+str(self.age))

    @classmethod
    def get_subjects(cls):
        return cls.subjects


s= Student('A',12)
s.display()
print(Student.get_subjects())
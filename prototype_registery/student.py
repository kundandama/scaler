class Student:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def __copy__(self):
        return Student(self.name, self.age)

    def clone(self):
        return self.__copy__()


class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Course : {self.course}")

    def introduce(self):
        print(f"Hi, I am {self.name} and I am studying {self.course}.")

s1 = Student("Vansh", 20, "BCA")

s1.display_details()
s1.introduce()

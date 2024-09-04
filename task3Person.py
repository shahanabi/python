class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Student(Person):
    def __init__(self, name, age, gender, major, gpa):
        super().__init__(name, age, gender)
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return f"Name: {self.name}, Major: {self.major}, GPA: {self.gpa}"


person = Person("sahanabi", 20, "Female")
print(person)  

student = Student("sahanabi", 20, "female", "Computer Application", 3.8)
print(student) 

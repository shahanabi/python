class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee(Person):
    def __init__(self, name, age,employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id
        

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Employee_id: {self.employee_id}"


p = Person("sahanabi", 20)
print(p)  

E = Employee("sahanabi", 20,"em_34")
print(E) 

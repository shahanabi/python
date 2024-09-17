# single inheritance


# class Animal:
#     def sound(self):
#         return "dog name is Tiger" 

# class Dog(Animal):
#     def sound(self):
#         return "he is say Boww"

# a = Animal()
# print(a.sound())  
# d = Dog()
# print(d.sound())  



#  multilevel inheritance


# class Vehicle:
#     def __init__(self,model):
#         self.model = model

#     def display(self):
#         print(f"Vehicle Model: {self.model}")

# class Car(Vehicle):
#     def __init__(self, model,color):
#         super().__init__(model)
#         self.color=color

#     def display(self):
#         super().display()
#         print(f"car color: {self.color}")

# class ElectricCar(Car):
#     def __init__(self, model, color,battery_capacity):
#         super().__init__(model, color)
#         self.battery_capacity=battery_capacity

#     def display(self):
#         super().display()
#         print(f"Battery Capacity: {self.battery_capacity} kWh")

# ec=ElectricCar("Hyundai Ioniq","Black",72.6)
# ec.display()



# hierarchical inheritance

# import math

# class Shape:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         print(f"Shape: {self.name}")

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__("Circle")
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

#     def display(self):
#         super().display()
#         print(f"Area: {self.area()}")

# class Square(Shape):
#     def __init__(self, side):
#         super().__init__("Square")
#         self.side= side

#     def area(self):
#         return self.side ** 2

#     def display(self):
#         super().display()
#         print(f"Area: {self.area()}")


# c=Circle(3)
# s=Square(4)
# c.display()
# s.display()



#hybrid inheritance

class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name,employee_id):
        super().__init__(name)
        self.employee_id = employee_id
        

class Student(Person):
    def __init__(self, name,student_id):
        super().__init__(name)
        self.student_id = student_id
        

class Intern1(Employee):
    def __init__(self, name,employee_id):
        
        Employee.__init__(self, name,employee_id)
        # Student.__init__(self, name,student_id)

class Intern(Student):
    def __init__(self, name,student_id):
        
        # Employee.__init__(self, name,employee_id)
        Student.__init__(self, name,student_id)


i=Intern1("sahanabi","em_42")
I=Intern("sahanabi","st_21")
print(f"employee name: {i.name} ,employee id: {i.employee_id} ,,      student name:{I.name}  ,student id:{I.student_id}")
# I=Intern("sahanabi","st_21")
# I.display()
# print(I)

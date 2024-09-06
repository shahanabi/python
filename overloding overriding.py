# class Shape:
#     def area(self):
#         return 0

# class Circle(Shape):
#     def _init_(self, radius):
#         self.radius = radius
    
#     def area(self):
#         return 3.14 * (self.radius ** 2)
    
# class Rectangle(Shape):
#     def _init_(self, width, height):
#         self.width = width
#         self.height = height
    
#     def area(self):
#         return self.width * self.height

# c = Circle(6)
# r = Rectangle(7,2)

# print(f"Area of the circle: {c.area()}")  
# print(f"Area of the rectangle: {r.area()}")




# class vehicle:
#     def speed():
#         return 0
    
# class car(vehicle):
#     def _init_(self,time,distance):
#         self.time=time
#         self.distance=distance
#     def speed(self):
#         return self.distance/self.time

# class bike(vehicle):
#     def  _init_(self,time,distance):
#         self.time=time
#         self.distance=distance
#     def speed(self):
#         return self.distance/self.time
    
# Car = car(2,10)
# Bike= bike(3,12)
# print(Car.speed())
# print(Bike.speed())






# class product:
#     def _init_(self,name,price):
#         self.name=name
#         self.price=price
#     def final_price(self):
#         return self.price

# class discountedproduct(product):
#     def _init_(self, name, price,discount):
#         super()._init_(name, price,)
#         self.discount=discount

#     def final_price(self):
#         return self.price-((self.discount*self.price)/100)

# class seasonalproduct(product):
#     def _init_(self, name, price,seasonaldiscount):
#         super()._init_(name, price)
#         self.seasonaldiscount=seasonaldiscount

#     def final_price(self):
#         return self.price-((self.seasonaldiscount*self.price)/100)

# p=product("laptop",45000)
# d=discountedproduct("laptop",45000,10)
# s=seasonalproduct("laptop",45000,5)


# print("orginal prise :",p.final_price())
# print("discounted prise :",d.final_price())
# print("seasonal discounted prise :",s.final_price())




# class polygon:
#     def perimeter (self):
#         return 0
    
# class triangle (polygon):
#     def _init_(self,side1,side2,side3):
#         self.side1=side1
#         self.side2=side2
#         self.side3=side3

#     def perimeter(self):
#         return self.side1+self.side1+self.side3
    
# class square(polygon):
#     def _init_(self,side):
#         self.side=side

#     def perimeter(self):
#         return 4*self.side
    

# t=triangle(3,4,5)
# s=square(7)

# print("perimeter of triangle :",t.perimeter())
# print("perimeter of square :",s.perimeter())






class employee:
    def _init_(self,salary):
        self.salary=salary

    def Salary(self):
        return self.salary
    
class manager(employee):
    def _init_(self, name, salary,bonus):
        super()._init_(salary)
        self.name=name
        self.bonus=bonus

    def Salary(self):
        return self.salary+self.bonus
    
class developer (employee):
    def _init_(self, Name, salary,Bonus):
        super()._init_( salary)
        self.Name=Name
        self.Bonus=Bonus

    def Salary(self):
        return self.salary+self.Bonus
    

e=employee(20000)
m=manager("Shemeema",70000,2000)
d= developer("thesni",50000,1000)

print("basic salary :",e.Salary())
print("salary of manager :",m.Salary())
print("salary of developer :",d.Salary())
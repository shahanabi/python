class circle:
    def _init_(self,radius):
        self.radius=radius

    def area(self):
        return 3.14 (self.radius*2)
c=circle(5)
print("area of cirle:",c.area())







class rectangle:
    def _init_(self,length,width):
        self.length = length
        self.width = width

    def perimeter(self):
        perimeter = 2*(self.length+self.width)
        return perimeter
    
    def area(self):
        area = self.length*self.width
        return area
    
r=rectangle(2,3)
print("perimeter of rectangle :",r.perimeter())
print("area of rectangle :",r.area())







class investment:
    def _init_(self,principal,time,rate):
        self.principal = principal
        self.rate = rate
        self.time = time

    def compound_interest(self):
        amount = self.principal*(1+(self.rate/100))**self.time
        return amount
    
i= investment (4000,10,2)
print("Amount:",i.compound_interest())
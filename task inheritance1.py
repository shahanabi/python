class Shape:
    def area(self):
        return 0

class square(Shape):
    def _init_(self, side):
        super()._init_()
        self.side=side
    
    def area(self):
        return self.side**2
    
class Rectangle(Shape):
    def _init_(self,width,height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
s=square(5)
r=Rectangle(7,9)
print(s.area())
print(r.area())
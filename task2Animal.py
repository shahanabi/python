class Animal:
    def _init_(self, name):
        self.name = name
 
    def make_sound(self):
        pass
 
 
class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow"
 
c = Cat("kitty")  
print(c.make_sound())

   

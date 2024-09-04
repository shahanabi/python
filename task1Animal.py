class animal:
    def _init_(self,name,species,age):
        self.name=name
        self.species=species
        self.age=age
    
class dog(animal):
    def _init_(self,name,species,age,breed):
        super()._init_(name,species,age)
        self.breed=breed

    def _str_(self):
        return f"Is a {self.name} and its breed is {self.breed}"
    
d=dog("gimmi","canis",1,"German")
print(d)
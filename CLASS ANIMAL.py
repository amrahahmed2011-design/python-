from abc import ABC, abstractmethod
#CREATE A BASE CLASS
class animal(ABC):
    #ABSTRACT METHOD
    #SHOULD BE IPLEMENTED IN SUBCLASSES
    def move(self):
        pass
#SUB CLASSES
class human(animal):
    #IMPLEMENT ABSTRACT METHOD
    def move(self):
        print("I CAN WALK AND RUN")
class lion(animal):
    def move(self):
        print("I CAN ROAR")
class snake(animal):
    def move(self):
        print("I CAN SLITHER")
class dog(animal):
    def move(self):
        print("I CAN BARK")
class cat(animal):
    def move(self):
        print("I CAN MEOW")
class fish(animal):
    def move(self):
        print("I CAN SWIM")
class bird(animal):
    def move(self):
        print("I CAN FLY")
class frog(animal):
    def move(self):
        print("I CAN JUMP")
class horse(animal):
    def move(self):
        print("I CAN GALLOP")
class elephant(animal):
    def move(self):
        print("I CAN TRUMPET")
class monkey(animal):
    def move(self):
        print("I CAN CLIMB AND SWING")
#CREATING OBJECTS
r = human()
r.move()
p = lion()
p.move()
u= snake()
u.move()
v = dog()
v.move()
w = cat()
w.move()
x = fish()
x.move()
y = bird()
y.move()
z = frog()
z.move()
a = horse()
a.move()
b = elephant()
b.move()
c = monkey()
c.move()
#CREATE A FAMILY CLASS WITH SHARED FAMILY TRAITS
class Familymember:
    def __init__(self, height , eye_color):
        self.height = height
        self.eye_color = eye_color
    def show_traits(self):
        print("height :", self.height)
        print("eye color :", self.eye_color)
    #create a child class that inherits from the family class
class kid(Familymember):
        #give kid its own details , plus the inherited traits
    def __init__(self, name, age , height, eye_color):
        super().__init__(height, eye_color)
        self.name = name
        self.age = age
    #override the show traits methods that only kid has
    def show_traits(self):
        print("NAME:", self.name)
        print("AGE:", self.age)
        super().show_traits()
    #ADD A BRANDE NEW METHOD THAT THE ONLY KID HAS
    def favourite_hobby(self, hobby):
        print("FAVOURITE HOBBY:", hobby)
    #CREATE A KID OBJECT WITH REAL FAMILY TRAITS
child = kid("Amrah", 14, 133, "BLACK")
    #CALL THE OVERIDDEN METHOD TO SHOW THE KID'S TRAITS
child.show_traits()
child.favourite_hobby("ALWAYS SCOLDING")
#CHECK WEATHER THE KID IS ACTUALLY AN INSTANCE OF THE FAMILY CLASS
print("IS THE KID REALLY A SUBCLASS OF FAMILY MEMBER?", issubclass(kid, Familymember))

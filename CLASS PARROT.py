#CREATING A CLASS PARROT
class parrot :
    #CLASS ATTRIBUTES
    species = "bird"
    #INITIALIZE ATTRIBUTE
    def __init__(self,name,age):
        self.name = name
        self.age = age
pi = parrot("ping",9)
po = parrot("pong",10)
#ACCESS THE ATTRIBUTES
print("PING IS A {}".format(pi.species))
print("PONG IS ALSO A {}".format(po.species))
#ACCESS THE INSTANCE ATTRIBUTES
print("{} IS {} YEARS OLD".format(pi.name,pi.age))
print("{} IS {} YEARS OLD".format(po.name,po.age))
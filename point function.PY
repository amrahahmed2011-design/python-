#CREATE CLASS
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        #method to print co ordinates 
    def __str__(self):
            return "({0},{1})".format(self.x , self.y)
#create object
p1 = Point(567,890)
print(p1)
#CREATE CLASS
class vehicle :
    #CREATE INIT METHOD
    def __init__(self, max_speed,mileage):
        #BIND THE ARGUMENTS
        self.max_speed = max_speed

        self.mileage = mileage
        #OBJECT CREATION
modelY = vehicle(120,70)
#ACCESSING THE OBJECT ATTRIBUTES
print("MODEL MAX SPEED :",modelY.max_speed)
print("MODEL MILEAGE :",modelY.mileage)
        
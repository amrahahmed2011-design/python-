#CREATING A CLASS
class IOSstring():
    #CONSTRUCTOR TO SET A DEFAULT VALUE
    def __init__(self):
        self.str1 = ""
        #FUNCTION TO GET INPUT FROM THE USER
    def get_string(self):
        self.str1 = input("ENTER a string : ")
        #FUNCTION TO PRINT IN UPPER CASE
    def print_string(self):
        print("RESULT IS :",self.str1.upper())
        #CREATING OBJECT
str1 = IOSstring()
str1.get_string()
str1.print_string()
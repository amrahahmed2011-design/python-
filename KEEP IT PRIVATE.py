#CLASS CREATION
class myClass:

    #private variable
    __privateVar = 578;

    #private method
    def __privmeth(self):
        print("This is a private method");
    #function to print the value of private variable
    def hello(self):
        print("PRIVATE VARIABLE VALUE: ", self.__privateVar);
#OBJECT CREATION AND METHOD CALL
foo = myClass()
foo.hello()
foo.__privmeth()  # This will raise an Error since __privmeth is private

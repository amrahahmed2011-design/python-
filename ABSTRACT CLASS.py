#IMPORT NECESSARY MODULES
from abc import ABC,abstractmethod
#CREATE BASE CLASS
class absclass(ABC):
    #function to print a value
    def print(self,x):
        print("THE VALUE IS:",x)
    #ABSTRACT METHOD
    @abstractmethod
    def task(self):
        print("WE ARE INSIDE THE ABSTRACT METHOD")
    #CREATE SUBCLASS
class test_class(absclass):
    #IMPLEMENT TES_CLASS METHOD
    def task(self):
        print("WE ARE INSIDE THE TEST_CLASS ABSTRACT METHOD")
    #OBJECT OF TEST_CLASS
test_objects = test_class()
test_objects.task()
test_objects.print(349)
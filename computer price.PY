class computer:
    def __init__(self):
        self.__maxprice = 750
    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))
    def setmaxprice(self,price):
        self.__maxprice = price
c = computer()
c.sell()
#change the price
c.__maxprice = 1000
c.sell()
#using setter function
c.setmaxprice(1200)
c.sell()
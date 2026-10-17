class book:
    def __init__(self, title, author, available):
        self.title = title
        self.author = author
        self.available = available
    def borrow(self):
        if self.available:
            self.available = False
            print("THE BOOK IS NOT AVAILABLE.")
            return True
        else:
            print("Sorry, that book is not available.")
            return False
    def return_book(self):
        self.available = True
        print("THE BOOK HAS BEEN RETURNED.")
    def show(self):
        if self.available:
            print(self.title,"is available")
        else:
            print(self.title,"is not available")
#create book objects
book1 = book("ENGLISH GRAMMAR","JAMES",True)
book2 = book("PYTHON PROGRAMMING","JOHN",True)
book3 = book("chemistry","JAMES",True)
book4 = book("physics","JAMES",True)
book5 = book("MATHS","JAMES",True)
#dosplay
book1.show()
book2.show()
book3.show()
book4.show()
book5.show()
book1.borrow()
book1.show()
book2.borrow()
book2.show()
book3.borrow()
book3.show()
book4.borrow()
book4.show()
book5.borrow()
book5.show()
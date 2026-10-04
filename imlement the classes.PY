class employee:
    def __init__(self, id, salary):
        self.id = id
        self.salary = salary
class salesEmployee(employee):
    def __init__(self, id,salary,sales):
        self.sales = sales
        super().__init__(id,salary)
    def output(self):
        print("ID:", self.id)
        print("SALARY:", self.salary)
        print("SALES:", self.sales)
manager = salesEmployee(14,30000,130)
manager.output()
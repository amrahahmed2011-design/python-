import math
def calculator (a, b, operation):
 try:
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "INVALID OPERATION"
     
 except ZeroDivisionError:
        return "ERROR: Division by zero is not allowed"
 except TypeError:
        return "ERROR: Invalid input types"
print("Simple Calculator")
print("Operations: add, subtract, multiply, divide")
print("calculator(a, b, operation)")
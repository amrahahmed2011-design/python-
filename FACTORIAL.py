def factorial(x):
    """This function calculates the factorial of a given number x."""
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x-1)
    
print(factorial.__doc__)
print("The factorial of 5 is:", factorial(5))
print("The factorial of 0 is:", factorial(0))
print("The factorial of 7 is:", factorial(7))
print("The factorial of 10 is:", factorial(10))
print("The factorial of 3 is:", factorial(3))
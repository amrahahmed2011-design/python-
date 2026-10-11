#create a class

# Account PIN Protection System

# PART 1: Create a class with private information
class Account:

    def __init__(self, owner, pin):
        self.owner = owner
        self.__pin = pin  # private attribute

    # Display account information safely
    def show_pin_status(self):
        print("Account Holder:", self.owner)
        print("The PIN is stored securely in the class.")

    # Update the PIN using a setter method
    def set_pin(self, updated_pin):
        if len(updated_pin) == 4 and updated_pin.isdigit():
            self.__pin = updated_pin
            print("Your PIN has been changed successfully.")
        else:
            print("Invalid PIN! Enter exactly 4 digits.")

    # Verify the entered PIN
    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("PIN is correct. Access granted.")
        else:
            print("Incorrect PIN. Access denied.")

    #Control how the object is displayed
    def __str__(self):
        return "Account Owner: " + self.owner



# Create an  object
my_account = Account("Riya", "1234")

# Display the account object
print(my_account)

# PART 8: Show the PIN storage status
my_account.show_pin_status()

# Try changing the private PIN from outside
my_account.__pin = "5678"
print("Attempted to change the PIN directly.")

# Check whether the original PIN is still active
my_account.check_pin("5678")
my_account.check_pin("1234")

# Change the PIN using the setter method
my_account.set_pin("5678")

# Verify the new PIN
my_account.check_pin("5678")

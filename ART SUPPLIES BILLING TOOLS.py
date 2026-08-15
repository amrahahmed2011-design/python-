# PART 1: Define a function with no arguments to welcome the customer
def welcome_customer():
    print("Welcome to the Creative Art Shop!")
    print("Find colours, brushes, papers, and more here.")

# PART 2: Call the welcome_customer function
welcome_customer()

# PART 3: Ask for the price per item and the number of items bought
price_per_item = float(input("Enter the price of one art item in dollars: "))
items_bought = int(input("Enter the number of art items you purchased: "))

# PART 4: Define a function that takes arguments and returns the total cost
def find_total(price, items):
    total = price * items
    return total

# PART 5: Call find_total and store the value it returns
total_cost = find_total(price_per_item, items_bought)

# PART 6: Use a built-in function to round the total, then print it
rounded_total = round(total_cost, 2)
print("Your Total is:", rounded_total)

# PART 7: Ask how much money the customer paid
amount_paid = float(input("Enter the money paid by the customer: "))

# PART 8: Define a function that takes arguments and returns the change due
def find_change(paid, total):
    change = paid - total
    return change

# PART 9: Call find_change and store the value it returns
change_due = find_change(amount_paid, rounded_total)
rounded_change = round(change_due, 2)

# PART 10: Define a function that returns a message based on items bought
def closing_message(items):
    if items >= 5:
        return "Awesome! You bought lots of supplies for your artwork."
    else:
        return "Thank you for shopping with us!"

# PART 11: Call closing_message and store the value it returns
final_message = closing_message(items_bought)

# PART 12: Print the final art supplies receipt
print("")
print("===== ART SHOP RECEIPT =====")
print("Item Price:", price_per_item)
print("Number of Items:", items_bought)
print("Total Amount:", rounded_total)
print("Money Paid:", amount_paid)
print("Change:", rounded_change)
print(final_message)
print("============================")
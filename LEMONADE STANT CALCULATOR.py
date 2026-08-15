def greet_customer():
    print("Welcome to the Lemonade Stand Calculator!")
    print("FREE Lemonade for everyone!")
#CALL THE GREET_CUSTOMER FUNCTION HERE
greet_customer()

price_per_cup = float(input("Enter the price per cup of lemonade: "))
cups_sold = int(input("Enter the number of cups sold: "))
def calculate_total(price_per_cup, cups_sold):
    total = price_per_cup * cups_sold
    return total
#CALL THE CALCULATE_TOTAL FUNCTION HERE
total_cost = calculate_total(price_per_cup, cups_sold)
#USE A BUILT-IN FUNCTION TO ROUND THE TOTAL COST TO 2 DECIMAL PLACES AND PRINT IT
rounded_total = round(total_cost, 2)
print("TOTAL COST : $", rounded_total)
#ASK HOW MUCH MONEY THE CUSTOMER PAID
amount_paid = float(input("Enter the amount of money the customer paid: "))

def calculate_change(amount_paid, total_cost):
    change = amount_paid - total_cost
    return change
#CALL THE CALCULATE_CHANGE FUNCTION HERE
change_due = calculate_change(amount_paid, total_cost)
rounded_change = round(change_due, 2)
print("CHANGE DUE : $", rounded_change)

def thankyou_message(cups):
    if cups >= 5:
        print("Thank you for your purchase! You get a free cookie!")
    else :
        print("Thank you for your purchase! Enjoy your lemonade!")
#CALL THE THANKYOU_MESSAGE FUNCTION HERE
closing_message =thankyou_message(cups_sold)

#PRINT THE FINAL LEMONADE STAND REPORT
print("=====================================")
print("\nLEMONADE STAND REPORT")
print("Price per cup: $", price_per_cup)
print("Total cups sold:", cups_sold)
print("amount paid: $", amount_paid)
print("Total revenue: $", rounded_total)
print("Change due: $", rounded_change)
print("closing message:", closing_message)
print("=====================================")

# Bill & Seating Helper

# PART 1: Define a function using positional arguments
def calculate_bill(amount, tip_percent):
    # Add the tip to the bill
    final_amount = amount * (1 + 0.01 * tip_percent)
    final_amount = round(final_amount, 2)
    print(f"Your final bill is ${final_amount}")
    return final_amount


# PART 2: Call the function with positional arguments
calculate_bill(200, 15)


# PART 3: Define a recursive function with a docstring
def seating_arrangements(number_of_guests):
    """This recursive function calculates seating arrangements for guests."""

    # Base case
    if number_of_guests <= 1:
        return 1

    # Recursive case
    return number_of_guests * seating_arrangements(number_of_guests - 1)


# PART 4: Print the function's docstring
print(seating_arrangements.__doc__)


# PART 5: Show seating arrangement results
print("Arrangements for 1 guest:", seating_arrangements(1))
print("Arrangements for 2 guests:", seating_arrangements(2))
print("Arrangements for 4 guests:", seating_arrangements(4))
print("Arrangements for 5 guests:", seating_arrangements(5))
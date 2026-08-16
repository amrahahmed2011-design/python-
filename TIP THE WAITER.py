def total_calc(bill_amount, tip_percentage):
#define function to calculate total amount including tip
  total = bill_amount + (bill_amount * tip_percentage / 100)
  total = round(total, 2)
  print("The total amount to be paid is: $", total)
#specify only bill amount
#default value for tip percentage is used
total_calc(100, 15)
def calculate_change(price,paid):
    change = paid - price
    return change
#SET THE SNACK PRICE AND GREET THE CUSTOMER
snack_price = 25
print("======SNACK VENDING MACHINE======")
print("THIS SNACK COSTS",snack_price,"CENTS")
print("ACCEPTED COINS: 1,5,10,25 CENTS")

total_inserted = 0
coins_inserted = 0
#REJECT ANY COINS THAT ARE INVALID
while True:
    coin = int(input("INSERT COIN: "))
    if coin!= 1 and coin != 5 and coin != 10 and coin != 25:
        print("INVALID COIN. PLEASE INSERT A VALID COIN.")
        continue
# ADD THE VALID COIN TO THE RUNNING TOTAL
    total_inserted += coin
    coins_inserted += 1
    print("TOTAL INSERTED: ", total_inserted, "CENTS")

#STOP ASKING FOR COINS WHEN ENOUGH HAS BEEN INSERTED
    if total_inserted >= snack_price:
        break
#WORK OUT THE CHANGE DUE AND THANK THE CUSTOMER FOR THEIR PURCHASE
change_due = calculate_change(snack_price,total_inserted)
print("THANK YOU FOR YOUR PURCHASE!")
#NOTHING EXTRA TO DO WHEN THE CHANGE DUE IS ZERO
if change_due==0:
    pass
else:
    print("YOUR CHANGE IS: ", change_due, "CENTS")
#PRINTING THE SUMMARY OF THE TRANSACTION
print("=======TRANSACTION SUMMARY=======")
print("SNACK PRICE: ", snack_price, "CENTS")
print("TOTAL INSERTED: ", total_inserted, "CENTS")
print("CHANGE DUE: ", change_due, "CENTS")
print("COINS INSERTED: ", coins_inserted)

items = ["pencils","sharpens","notebooks","erasers","markers"]
stock_counts = [100,50,0,30,20]
#PAIR THE ITEMS
inventory = {items: count for items, count in zip(items, stock_counts)}
print("FULL INVENTORY:",inventory)
#FILTER ONLY THE ITEMS THAT ARE STILL IN THE STOCK
in_stock_items = {item for item in items if inventory[item] > 0}
print("IN STOCK:",in_stock_items)
#ASK THE SHOPER WHICH ITEM THEY WANT TO BUY
item_to_buy = input("Which item would you like to buy? ")
#CHECK IF THE ITEM IS IN STOCK
if item_to_buy not in inventory or inventory[item_to_buy] == 0:
    print("Sorry, that item is out of stock.")
    exit()
#CREATE THE PRICES AND ASK FOR MARKUP AMOUNT
PRICES = [20,20,100,10,70]
markup = int(input("Enter the markup amount: "))
#APPLY THE MARKUP TO THE PRICES USING MAP
marked_up_prices = list(map(lambda p: p + markup, PRICES))
print("MAEKED UP PERICES :",marked_up_prices)
#FIND TEH MARKEDUP PRICES OF THE CHOSEN ITEMS
item_index = items.index(item_to_buy)
chosen_price = marked_up_prices[item_index]
print("The price of", item_to_buy, "after markup is:", chosen_price)
#REDUCE THE STOCK COUNT OF THE CHOSEN ITEM BY 1
inventory[item_to_buy] = inventory[item_to_buy] - 1
print("Updated inventory after purchase:", inventory)
#PRINT THE FINAL STORE SUMMARY
print("---------------------------------")
print("FINAL STORE SUMMARY:")
print("ITEMS BOUGHT:", item_to_buy)
print("PRICE PAID:", chosen_price)
print("REMAINING STOCK:", inventory)
print("---------------------------------")
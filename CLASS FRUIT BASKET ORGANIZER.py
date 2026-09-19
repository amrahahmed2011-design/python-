#CREATE TWO FRUIT BASKETS AS SETS
basket1 = {"apple", "banana", "orange", "kiwi"}
basket2 = {"banana", "grape", "kiwi", "mango"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)
# ADDING A FRUIT TO BASKET1
basket1.add("pear")
print("Basket 1 after adding pear:", basket1)
# FINDING THE COMMON FRUITS BETWEEN THE TWO BASKETS
common_fruits = basket1.intersection(basket2)
print("Common fruits:", common_fruits)
#CREAT AN ARRAY OF FRUIT COUNT 
import array as arr
fruit_count = arr.array('i', [3,7,8,2,5])
print("Fruit counts:", fruit_count)
# ADD NEW ITEMS TO THE FRUIT COUNT ARRAY
new_fruits = arr.array('i', [4, 6])
fruit_count.insert(6, 4)
fruit_count.append(8)
print("Updated fruit counts:", fruit_count)
# COUNT THE NUMBER OF FRUITS IN THE BASKETS
total_fruits_basket1 = len(basket1)
total_fruits_basket2 = len(basket2)
print("Total fruits in Basket 1:", total_fruits_basket1)
print("Total fruits in Basket 2:", total_fruits_basket2)
# REVERSE THE ORDER OF THE FRUIT COUNT ARRAY
fruit_count.reverse()
print("Reversed fruit counts:", fruit_count)
# PRINT THE FINAL SUMMARY
print("")
print("-------------------")
print("basket 1:", basket1)
print("BASKET 2 :",basket2)
print("COMMON FRUITS",common_fruits)
print("FRUIT COUNT :", fruit_count)
print("--------------------")
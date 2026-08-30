import random
playing = True
number = str(random.randint(0,9))

print("I WILL GENERATE A NUMBER FROM 0 TO 9 AND YOU HAVE TO GUESS THAT NUMBER")

while playing:
    guess = input("GIVE ME YOUR BEST GUESS")
    if number == guess:
        print("YOU WON!!!")
        print("THE NUMBER WAS",number)
        break
    else:
        print("YOUR GUESS IS NOT RIGHT")

import random
while True:
    user_action = input("ENTER CHOICE (ROCK,PAPERS,SCISSORS): ")
    possible_action = ["rock","papers","scissors"]
    computer_action = random.choice(possible_action)
    print(f"YOU CHOSE {user_action}, COMPUTER CHOSE {computer_action}.")


    if user_action == computer_action:
        print(f"BOTH PLAYERS SELECTED{user_action}, ITS A TIE!!")
    elif user_action== "rock":
        if computer_action == "scissors":
            print("ROCK SMASHES SCISSORS,YOU WIN")
        else:
            print("PAPER COVERS ROCK,YOU LOOSE!")

    elif user_action== "paper":
            if computer_action == "rock":
                print("PAPER COVERS ROCK,YOU WIN")
            else:
                print("SCISSORS CUT PAPER,YOU LOOSE!")


    elif user_action== "scissors":
                if computer_action == "paper":
                    print("SCISSORS CUTS PAPER,YOU WIN")
                else:
                    print("ROCK SMASHES SCISSORS,YOU LOOSE!")
    play_again = input("DO YOU WANT TO PLAY AGAIN(Y/N):")
    if play_again != "Y":
         break
         
    



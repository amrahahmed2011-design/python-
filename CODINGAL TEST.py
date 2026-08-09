import random


number = random.randint(1, 50)
lives = 5

print("Guess the number between 1 and 50!")

while lives > 0:
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("🎉 You won!")
        break

    if guess < number:
        print("Too low! Try a bigger number.")
    else:
        print("Too high! Try a smaller number.")

    lives = lives - 1
    print("Lives left:", "❤️" * lives)

if lives == 0:
    print("Game Over!")
    print("The number was:", number)
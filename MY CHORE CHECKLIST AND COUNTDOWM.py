total_chores = 4
original_chores = total_chores
print(f"you have {original_chores} chores to do.")

completed_chores = 0
chore_number = 1

while completed_chores <= total_chores:

    if chore_number==1: next_chore = "Clean the kitchen"
    elif chore_number==2: next_chore = "Do the laundry"
    elif chore_number==3: next_chore = "Vaccum the living room"
    else: next_chore = "Take out the trash"

    answer=input(f"Have you completed {next_chore}? (yes/no): ")
    if answer == "yes":
        completed_chores += 1
        chore_number += 1
        print(f"Great! You have completed {completed_chores} chores.")
    else:
        print(f"Okay, you still have them to do.")

        print(f"You have {total_chores - completed_chores} chores left to do.")
        print()

print("==================ALL CHORES COMPLETED==================")
print(f"Congratulations! You have completed all {original_chores} chores.")

print("NOW LETS SAFELY PEEK AT THE AN INFINITE LOOP!")
text_value = 0
safty_counter = 0
while text_value <=0:
    print("This is an infinite loop! Be careful!")
    safty_counter += 1

    if safty_counter >= 5:
        print("Safety limit reached. Exiting loop.")
        break
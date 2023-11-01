### ROCK PAPER SICCORS GAME
import random

list1 = ["Rock", "Paper", "Scissors"]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)
print("This is Computer Choice " + list1[computer_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number")
elif  user_choice == 0 and computer_choice == 2:
    print("You Win")
elif computer_choice > user_choice:
    print("Computer Wins!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice == user_choice:
    print("Its a Draw")
elif user_choice > computer_choice:
    print("You win")

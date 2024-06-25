from art import logo
from game_data import data 
import random
from replit import clear


### Higher Lower game Solution 

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return(f"{account_name}, a {account_descr}, from {account_country}")

def check_answer(user_input, a_followers, b_followers):
    """"use if statement to check if user is correct """
    if a_followers > b_followers:
        return user_input == "a"
    else: 
        return user_input == "b"
    
score = 0 
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

   
    account_a = account_b
    account_b = random.choice(data)


    while account_a == account_b: 
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(f"Against B: {format_data(account_b)}")


    user_input=input("Who has more followers A or B: ").lower()

    a_follower_count = account_a ["follower_count"]
    b_follower_count = account_b ["follower_count"]
    is_correct = check_answer(user_input, a_follower_count, b_follower_count)
 
    clear ()

    if is_correct:
        score += 1
        print(f"You are Right. Current score: {score}")
    else: 
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")
   

### Treasure Island 
print ("Welcome to Treasure Island\n Your mission is to find the treasure")
user_input1 = input("Choose either left of right ").lower()
if user_input1 == "left": 
    print("you fell in a hole and Died")
    print("GAME OVER")
else:
    user_input2 = input ("You come to a river, would you like to swim to wait for a Boat ").lower()
    if user_input2 == "swim":
        print("you got eaten by a fish and Died ")
        print("GAME OVER")
    else:
        user_input3 = input ("You see a Red and Blue door, Please pick one ").lower()
        if user_input3 == "red":
            print("you Died")
            print("GAME OVER")
        else:
            print("YOU FOUND THE TREASURE, WELL DONE ")

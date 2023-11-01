### Tip Calculator Program 
print("Welcome to the Tip calculator\n")
user_input = float(input("What is the total bill? "))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12 or 15 "))
final_tip = tip_percentage / 100 
total_tip_amount = user_input * final_tip
total_bill = user_input + total_tip_amount
total_users = float(input("How many people should split the bill? "))
bill_per_person = total_bill/total_users
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person will pay ${final_amount}")

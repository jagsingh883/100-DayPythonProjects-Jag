### Password generator
import random

print ("Welcome to the Password Generator")
letters = int(input("How many letters woud you like in your password?\n"))
symbols = int(input("How many symbols woud you like in your password?\n"))
numbers = int(input("How many numbers woud you like in your password?\n"))

list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list2 = ['!','@','#', '$','%','%','^','&','*','(',')']
list3 = ['0','1','2','3', '4', '5', '6' ,'7' '8', '9']

password = []

for char in range (1, letters + 1):
    password += random.choice(list1)
for char in range (1, symbols + 1):
    password += random.choice(list2)
for char in range (1, numbers + 1):
    password += random.choice(list3)

random.shuffle(password)

final_pass = ""
for char in password:
    final_pass += char

print(final_pass)
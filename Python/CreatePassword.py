import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']

print("Welcome to Password Generator!")

nr_letter = int(input("Home many letters would you like in your Password?\n"))

nr_numbers = int(input("Home many numbers would you like in your Password?\n"))

nr_symbols = int(input("Home many symbols would you like in your Password?\n"))

password_list = []

for char in range(1, nr_letter+1):
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers+1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

#print(password_list)
#random.shuffle(password_list)
#print(password_list)

password = ""

for char in password_list:
    password += char

print(f"Your Password is: {password}")
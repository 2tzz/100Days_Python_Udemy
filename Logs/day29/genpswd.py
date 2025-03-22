
import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password_list = []

letter_list = [char for char in letters if len(password_list) < random.randint(8, 10)]
symbol_list = [char for char in numbers if len(password_list) < random.randint(2, 4)]
number_list = [char for char in symbols if len(password_list) < random.randint(2, 4)]

password_list = letter_list + symbol_list + number_list

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
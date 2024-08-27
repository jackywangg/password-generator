import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
special_characters = "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

upper, lower, numbers, s_char = True, True, True, True

print("Please type Yes/No for each of the following character types you want to include: ")

## Asks user if they want to include uppercase letters.
print("Do you want to include UPPERCASE letters?")
upper_val = input("").lower()
if upper_val == "yes":
    upper = True
else:
    upper = False

## Asks user if they want to include lowercase letters.
print("Do you want to include LOWERCASE letters?")
lower_val = input("").lower()
if lower_val == "yes":
    lower = True
else:
    lower = False

## Asks user if they want to include numbers.
print("Do you want to include NUMBERS?")
number_val = input("").lower()
if number_val == "yes":
    numbers = True
else:
    numbers = False

## Asks user if they want to include special characters.
print("Do you want to include SPECIAL CHARACTERS?")
special_val = input("").lower()
if special_val == "yes":
    s_char = True
else:
    s_char = False

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if numbers:
    all += digits
if s_char:
    all += special_characters

length = 5
amount = 5

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
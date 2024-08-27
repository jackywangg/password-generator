import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
special_characters = "#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
length = 0
amount = 0
all = ""

upper, lower, numbers, s_char = False, False, False, False

print("Please type Yes/No for each of the following character types you want to include: ")

while not (upper or lower or numbers or s_char):
    print("You MUST select at least one character type.")

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
    
    ## Ensures that there must be at least one character type selected
    if not (upper or lower or numbers or s_char):
        print("You have selected " + "Yes " + "for none of the character types. Please try again.")
    print("")

## Prints the list of character types the user has selected
print("You have selected the following character types: ")
if upper:
    print("UPPERCASE letters")
if lower:
    print("LOWERCASE letters")
if numbers:
    print("NUMBERS")
if s_char:
    print("SPECIAL CHARACTERS")

while True:
    ## Asks user about the password's length.
    print("How many characters (must be greater than 0) do you want your password to be?")
    while True:
        pass_length = int(input("Password Length: "))
        if pass_length <= 0:
            print("You must enter a valid number. Please try again.")
        else:
            length = pass_length
            break

    ## Asks user about how many passwords to generate.
    print("How many passwords (must be greater than 0) do you want to generate?")
    while True:
        pass_amount = int(input("Number of Passwords: "))
        if pass_amount <= 0:
            print("You must enter a valid number. Please try again")
        else:
            amount = pass_amount
            break
    break

## Generates password(s) given the user's requirements
while True:
    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if numbers:
        all += digits
    if s_char:
        all += special_characters

    for x in range(amount):
        password = "".join(random.sample(all, length))
        print(password)

    new_set = input("Generate new set? (Yes/No): ").lower()
    if (new_set == "yes"):
        continue
    else:
        break

print("Thank you for using Password Generator!")
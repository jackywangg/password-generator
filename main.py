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
    while True:
        print("Do you want to include UPPERCASE letters?")
        upper_val = input("").lower()
        if upper_val == "yes":
            upper = True
            break
        elif upper_val == "no":
            upper = False
            break
        else:
            print("Not a valid selection. Please try again.")

    ## Asks user if they want to include lowercase letters.
    while True:
        print("Do you want to include LOWERCASE letters?")
        lower_val = input("").lower()
        if lower_val == "yes":
            lower = True
            break
        elif lower_val == "no":
            lower = False
            break
        else:
            print("Not a valid selection. Please try again.")


    ## Asks user if they want to include numbers.
    while True:
        print("Do you want to include NUMBERS?")
        number_val = input("").lower()
        if number_val == "yes":
            numbers = True
            break
        elif number_val == "no":
            numbers = False
            break
        else:
            print("Not a valid selection. Please try again.")

    ## Asks user if they want to include special characters.
    while True:
        print("Do you want to include SPECIAL CHARACTERS?")
        special_val = input("").lower()
        if special_val == "yes":
            s_char = True
            break
        elif special_val == "no":
            s_char = False
            break
        else:
            print("Not a valid selection. Please try again.")
    
    ## Ensures that there must be at least one character type selected
    if not (upper or lower or numbers or s_char):
        print("You have selected " + "Yes " + "for none of the character types. Please try again.")
    print("")

## Prints the list of character types the user has selected
print("You have selected the following character types: ")
if upper:
    all += uppercase_letters
    print("UPPERCASE letters")
if lower:
    all += lowercase_letters
    print("LOWERCASE letters")
if numbers:
    all += digits
    print("NUMBERS")
if s_char:
    all += special_characters
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
    for _ in range(amount):
        char_list = []

        if upper:
            char_list.append(random.choice(uppercase_letters))
        if lower:
            char_list.append(random.choice(lowercase_letters))
        if numbers:
            char_list.append(random.choice(digits))
        if s_char:
            char_list.append(random.choice(special_characters))

        ## append rest of password with random characters
        while len(char_list) < length:
            char_list.append(random.choice(all))

        random.shuffle(char_list)

        password = "".join(char_list)
        print(password)
    while True:
        new_set = input("Generate new set? (Yes/No): ").lower()
        if (new_set == "yes"):
            break
        elif (new_set == "no"):
            print("Thank you for using Password Generator!")
            exit()
        else:
            print("You must enter a valid selection. Please try again.")
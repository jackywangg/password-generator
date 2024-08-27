import random
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation
length = 0
amount = 0
all = ""

## Default these values to False. 
upper, lower, numbers, s_char = False, False, False, False

print("Please type Yes/No for each of the following character types you want to include: ")

while not (upper or lower or numbers or s_char):
    print("[You MUST select at least one character type.] \n ")

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

## Asks user for the password's length.
def get_password_length():
    while True:
        print("How many characters (must be greater than 0) do you want your password to be?")
        while True:
            try:
                pass_length = int(input("Password Length: "))
                if pass_length <= 0:
                    print("You must enter a valid number. Please try again.")
                elif pass_length < 8:
                    while True:
                        print("\nWe suggest that your password is at least 8 characters long. Do you wish to proceed with a length of " + str(pass_length) + " or choose a new length? (Continue/New Length)")
                        keep_length = input().lower()
                        if keep_length == "continue":
                            return pass_length
                        elif (keep_length == "new length"):
                            continue
                        else:
                            print("You must choose a valid selection. Please try again.")
                            continue
                else:
                    return pass_length
            except:
                print("Please choose a valid (numerical) password length.")

def get_password_amount():
    while True:
        ## Asks user about how many passwords to generate.
        print("How many passwords (must be greater than 0) do you want to generate?")
        while True:
            try:
                pass_amount = int(input("Number of Passwords: "))
                if pass_amount <= 0:
                    print("You must enter a valid number. Please try again.")
                else:
                    return pass_amount
            except:
                print("Please choose a valid number of passwords to generate.")

## Generates password(s) given the user's requirements
while True:
    length = get_password_length()
    amount = get_password_amount()
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
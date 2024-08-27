import random
import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
special_characters = string.punctuation
length = 0
amount = 0

## Default these values to False. 

def get_user_input(prompt):
    while True:
        val = input(prompt + "\n").lower()
        if val == "yes":
            return True
        elif val == "no":
            return False
        else:
            print("Not a valid selection. Please try again.")

def get_user_preferences():
    preferences = {
        "upper" : False,
        "lower" : False,
        "numbers": False,
        "s_char": False,
        "all" : ""
    }

    print("Please type Yes/No for each of the following character types you want to include: ")

    while not (preferences["upper"] or preferences["lower"] or preferences["numbers"] or preferences["s_char"]):
        print("[You MUST select at least one character type.] \n ")
        preferences["upper"] = get_user_input("Do you want to include UPPERCASE letters?")
        preferences["lower"] = get_user_input("Do you want to include LOWERCASE letters?")
        preferences["numbers"] = get_user_input("Do you want to include NUMBERS?")
        preferences["s_char"] = get_user_input("Do you want to include SPECIAL CHARACTERS?")
        
        ## Ensures that there must be at least one character type selected
        if not (preferences["upper"] or preferences["lower"] or preferences["numbers"] or preferences["s_char"]):
            print("You have selected " + "Yes " + "for none of the character types. Please try again.")
        print("")

    ## Prints the list of character types the user has selected
    print("You have selected the following character types: ")
    if preferences["upper"]:
        preferences["all"] += uppercase_letters
        print("UPPERCASE letters")
    if preferences["lower"]:
        preferences["all"] += lowercase_letters
        print("LOWERCASE letters")
    if preferences["numbers"]:
        preferences["all"] += digits
        print("NUMBERS")
    if preferences["s_char"]:
        preferences["all"] += special_characters
        print("SPECIAL CHARACTERS")
    
    return preferences

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

def password_generator():
    preferences = get_user_preferences()

    ## Generates password(s) given the user's requirements
    while True:
        length = get_password_length()
        amount = get_password_amount()
        while True:
            for _ in range(amount):
                char_list = []

                if preferences["upper"]:
                    char_list.append(random.choice(uppercase_letters))
                if preferences["lower"]:
                    char_list.append(random.choice(lowercase_letters))
                if preferences["numbers"]:
                    char_list.append(random.choice(digits))
                if preferences["s_char"]:
                    char_list.append(random.choice(special_characters))

                ## append rest of password with random characters
                while len(char_list) < length:
                    char_list.append(random.choice(preferences["all"]))

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

if __name__ == "__main__":
    password_generator()
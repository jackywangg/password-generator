import random

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
special_characters = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

upper, lower, numbers, s_char = True, True, True, True

all = ""

if upper:
    all += uppercase_letters
if lower:
    all += lowercase_letters
if numbers:
    all += digits
if special_characters:
    all += special_characters

length = 20
amount = 10

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)
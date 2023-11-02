import random
import string

# character sets for each type of character
capitals = string.ascii_uppercase
lowercase = string.ascii_lowercase
numbers = string.digits
symbols = "@#$%&+"

# generate password
password = random.choices(capitals, k=2) + random.choices(lowercase, k=5) + random.choices(numbers, k=2) + random.choices(symbols, k=1)
random.shuffle(password)
password = "".join(password)

# print the password
print("Generated password:", password)

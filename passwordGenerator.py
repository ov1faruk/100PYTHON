import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password=""

# for letter in range(1, nr_letters+1):
#     rand_letters = random.choice(letters)
#     password+=rand_letters

# for number in range(1, nr_numbers+1):
#     rand_numbers = random.choice(numbers)
#     password+=rand_numbers

# for symbol in range(1, nr_symbols+1):
#     rand_symbols = random.choice(symbols)
#     password+=rand_symbols

# random.shuffle(rand_pass:=list(password))
# rand_pass="".join(rand_pass)
# print(rand_pass)

#Alternative:
password=[]

for letter in range(1, nr_letters+1):
    rand_letters = random.choice(letters)
    password+=rand_letters

for number in range(1, nr_numbers+1):
    rand_numbers = random.choice(numbers)
    password+=rand_numbers

for symbol in range(1, nr_symbols+1):
    rand_symbols = random.choice(symbols)
    password+=rand_symbols
    
random.shuffle(password)

random_password=""

for char in password:
    random_password+=char
print("Your password is:"+random_password)


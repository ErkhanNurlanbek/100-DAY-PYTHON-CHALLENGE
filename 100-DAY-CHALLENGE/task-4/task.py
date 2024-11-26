import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
random_pass = ''
random_letter = -1

for i in range(0, nr_letters):
    random_int = random.randint(0, len(letters) - 1)
    a = str(letters[random_int])
    random_pass += a

for i in range(0, nr_symbols):
    random_int = random.randint(0, len(symbols) - 1)
    b = str(symbols[random_int])
    random_pass += b

for i in range(0, nr_numbers):
    random_int = random.randint(0, len(numbers) - 1)
    c = str(numbers[random_int])
    random_pass += c

r_l = list(random_pass)
shuffled_list = random.sample(r_l, len(r_l))
print(''.join(shuffled_list))
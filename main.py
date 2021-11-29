 #Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password2 = []

for text in range(nr_letters):
  randomText = random.randint(0,len(letters)-1)
  password2 += letters[randomText]

for symbol in range(nr_symbols):
  randomSymbol = random.randint(0,len(symbols)-1)
  password2 += symbols[randomSymbol]

for number in range(nr_numbers):
  randomNumber = random.randint(0,len(numbers)-1)
  password2 += numbers[randomSymbol]

print("Hard Level")
pass2 = ""
random.shuffle(password2)
for i in range(len(password2)):
  pass2 +=password2[i]

print(pass2)

import random

length = int(input("enter the length you want of your password:\n"))
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&*()_"
password = ''

for i in range(length):
    password += random.choice(characters)
print(f"Your password is: {password}")
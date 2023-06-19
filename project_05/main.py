# password generator

import random

print('Welcome To your password generator')

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ~!#$%^&*()_+=1234567890'
number = input('Amount of passwords to generate:')
number = int(number)

length = input('Input password length:')
length = int(length)

print('\n Here are your passwords')
for pwd in range(number):
    password = ''
    for  c in range(length):
        password += random.choice(char)
    print(password)
    
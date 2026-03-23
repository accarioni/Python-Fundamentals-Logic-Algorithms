# Exercise 7 - Truthy and Falsy values
# Purpose: Demonstrate how empty and non-empty values affect conditions and validate user input.

name = ''

while not name:
  name = input('Enter your name: ')

value = int(input('Enter a number: '))
if (value > 0):
  print('You entered a value greater than zero.')
else:
  print('You entered a value less than zero')
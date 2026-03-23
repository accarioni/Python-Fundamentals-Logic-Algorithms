# Exercise 3 - Even number validation: if the user input is an even number, returns "The number is even". Otherwise, returns "The number is odd".

num = int(input('Enter an integer number: '))

if (num % 2 == 0):
  print('The number is even')
else:
  print('The number is odd')
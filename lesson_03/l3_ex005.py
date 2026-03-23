# Exercise 5 - Basic calculator
# Purpose: Perform a mathematical operation based on user input.

num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
print('Possible operations: addition, subtraction, multiplication or division.')
operation = input('Choose an operation: ')

if(operation == 'Addition' or operation == 'addition'):
  print(f'Result: {num1 + num2}')

elif(operation == 'Subtraction' or operation == 'subtraction'):
  print(f'Result: {num1 - num2}')

elif(operation == 'Multiplication' or operation == 'multiplication'):
  print(f'Result: {num1 * num2}')

elif(operation == 'Division' or operation == 'division'):
  print(f'Result: {num1 * num2}')

else:
  print('The operation could not be completed')
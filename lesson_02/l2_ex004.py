# Exercício 4 - Reads the user’s fruit choice, validates it, and calculates the total price based on quantity and unit cost.

fruit_type = int(input('Which type of fruit do you want to buy? Enter 1 for apple, 2 for orange and 3 for banana. '))

if(fruit_type == 1):
  is_valid = True
  fruit = 'apple'
  fruit_price = 2.3

if (fruit_type == 2):
  is_valid = True
  fruit = 'orange'
  fruit_price = 3.6

if(fruit_type == 3):
  is_valid = True
  fruit = 'banana'
  fruit_price = 1.85

if(fruit_type != 1) and (fruit_type != 2) and (fruit_type != 3):
  is_valid = False
  print('Product does not exist.')

if(is_valid == True):
  fruit_quantity = int(input(f'How many units of {fruit} do you want to buy? '))
  final_value = fruit_quantity * fruit_price
  print(f'The total value of {fruit_quantity} units of {fruit} is R${final_value}')

elif(is_valid == False):
  print('The operation could not be completed. Please try again.')
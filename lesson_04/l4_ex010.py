# Exercise 10 - Problem (Snack bar ordering system)
# Purpose: Simulate a simple ordering system that accumulates the total cost until the user exits.

print('Available products:\n \nCoxinha - R$5.00\nPastel - R$7.00\nCoffee - R$4.00\nJuice - R$6.00')

order_count = 0
total_amount = 0

snack1 = 5
snack2 = 7
snack3 = 4
snack4 = 6

while (order_count >= 0):
  desired_product = input('Which product would you like to buy? \nTo finish the purchase, type "exit". ')
  desired_product_lower = desired_product.lower()
  order_count += 1
  if (desired_product_lower == 'coxinha'):
    total_amount += snack1
  elif (desired_product_lower == 'pastel'):
    total_amount += snack2
  elif (desired_product_lower == 'café'):
    total_amount += snack3
  elif (desired_product_lower == 'suco'):
    total_amount += snack4
  elif (desired_product_lower == 'exit'):
    print(f'\nThank you for your purchase! You need to pay: R${total_amount}.')
    break
  else:
    print('\nInvalid product')
  print(f'\nTotal amount: R${total_amount}')
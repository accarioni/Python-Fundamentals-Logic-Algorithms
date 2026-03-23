# Exercise 12 - Cinema ticket system
# Purpose: Calculate ticket prices based on age, accumulate total revenue, and compute average age.

print('Welcome to the cinema!')

people_count = 0
total_amount = 0
total_age = 0

while (people_count >= 0):
  age = int(input('\nEnter your age: \nTo stop ticket purchase, enter 0. '))
  people_count += 1
  total_age += age

  if ((age < 3) & (age > 0)):
    ticket_price = 0
    print('\nThe ticket is free')
    total_amount += ticket_price

  elif ((age >= 3) & (age <= 12)):
    ticket_price = 15
    print(f'\nThe ticket costs R${ticket_price}.')
    total_amount += ticket_price

  elif (age > 12):
    ticket_price = 30
    print(f'\nThe ticket costs R${ticket_price}.')
    total_amount += ticket_price

  elif (age == 0):
    print(f'Total number of people: {people_count}.\n')
    print(f'Total revenue = R${total_amount}.\n')
    print(f'Average age: {total_age / people_count}.\n')
    break
  
  
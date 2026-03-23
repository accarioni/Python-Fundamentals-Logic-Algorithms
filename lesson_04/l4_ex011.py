# Exercise 11 - Banknote decomposition
# Purpose: Break down a given amount into the minimum number of banknotes using a greedy approach.

amount_to_pay = int(input('What amount would you like to pay? '))

while (amount_to_pay):

  if (amount_to_pay >= 100):
    count_100 = amount_to_pay // 100
    amount_to_pay -= (count_100 * 100)
    print(f'Number of R$100.00 banknotes = {count_100}')
    if (amount_to_pay == 0):
      break

  if (amount_to_pay >= 50):
    count_50 = amount_to_pay // 50
    amount_to_pay -= (count_50 * 50)
    print(f'Number of R$50.00 banknotes = {count_50}')
    if (amount_to_pay == 0):
      break

  if (amount_to_pay >= 20):
    count_20 = amount_to_pay // 20
    amount_to_pay -= (count_20 * 20)
    print(f'Number of R$20.00 banknotes = {count_20}')
    if (amount_to_pay == 0):
      break

  if (amount_to_pay >= 10):
    count_10 = amount_to_pay // 10
    amount_to_pay -= (count_10 * 10)
    print(f'Number of R$10.00 banknotes = {count_10}')
    if (amount_to_pay == 0):
      break

  if (amount_to_pay >= 5):
    count_5 = amount_to_pay // 5
    amount_to_pay -= (count_5 * 5)
    print(f'Number of R$5.00 banknotes = {count_5}')
    if (amount_to_pay == 0):
      break

  if (amount_to_pay >= 1):
    count_1 = amount_to_pay // 1
    amount_to_pay -= (count_1 * 1)
    print(f'Number of R$1.00 banknotes = {count_1}')
    if (amount_to_pay == 0):
      break
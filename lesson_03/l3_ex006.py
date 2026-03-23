# Exercise 4 - Electricity bill calculation
# Purpose: Calculate the cost of electricity based on installation type and consumption.

print('Installation Types:')
print('R - Residential')
print('I - Industrial')
print('C - Commercial')
installation_type = input('What is the installation type? ')
kwh_consumed = float(input('Amount of kWh consumed: '))

if(installation_type == 'R'):
  if(kwh_consumed <= 500):
    consumption_value = kwh_consumed * 0.4
  elif(kwh_consumed > 500):
    consumption_value = kwh_consumed * 0.65

if(installation_type == 'I'):
  if(kwh_consumed <= 5000):
    consumption_value = kwh_consumed * 0.55
  elif(kwh_consumed > 5000):
    consumption_value = kwh_consumed * 0.6

if(installation_type == 'C'):
  if(kwh_consumed <= 1000):
    consumption_value = kwh_consumed * 0.55
  elif(kwh_consumed > 1000):
    consumption_value = kwh_consumed * 0.6

print(f'Amount to pay: R${consumption_value}')
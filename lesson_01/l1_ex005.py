# Exercise 5 - Vehicle rental cost calculation based on user input (using the input method)

rental_days = int(input('How many days was the vehicle rented? '))
distance_km = int(input('How many kilometers were traveled during the rental period? '))
rental_cost = rental_days * 60
distance_cost = distance_km * 0.15
total_amount = rental_cost + distance_cost

print(f'You must pay a total of R$ {total_amount}, where R$ {rental_cost} refers to the rental days and R$ {distance_cost} refers to the distance traveled.')
# Exercise 4 - Discount calculation based on user input (using the input method)

product_price = float(input('Enter the product price: '))
discount_percentage = float(input('Enter the discount percentage to be applied (0 - 100%): '))
final_price_with_discount = ((1 - discount_percentage/100) * product_price)

print(f'The final price of the product with discount is {final_price_with_discount}')
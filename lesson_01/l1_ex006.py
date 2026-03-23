# Exercise 6 - String manipulation using the len property

string_input = input('Enter a sentence: ')
string_length = len(string_input)
print(string_length)

half_string = string_input[:int(string_length/2)]
print(half_string[-2:])
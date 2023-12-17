# integer data type
price = 100
best_price = int(80)
print(type(price))
print(best_price)
print(isinstance(price, int))
print("")

# Float data type
Gpa = 3.45
y = float(3.98)
print(type(Gpa))
print(isinstance(y, float))
print("")

# complex data type
complex_value = 4 + 5j
print(type(complex_value))
print(complex_value.real)
print(complex_value.imag)
print("")

# Built-in functions for numbers

print(abs(Gpa))
print(abs(Gpa * -1))
print(round(Gpa))
print(round(Gpa, 1))
print("")

# import mathematical libraries
import math
print(math.pi)
print(math.sqrt(64))
print(math.ceil(Gpa))
print(math.floor(Gpa))
print("")

# casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
print("")

# NB: error if you attempt to cast incorrect data
# e.g zip_value = int("New York")
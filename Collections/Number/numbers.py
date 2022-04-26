'''
Numbers in Python are usually:
1. Integers
2. Float
3. Complex
'''
a = 443
b = 98.32
c = 10 + 9j
print("NUMBER TYPES: ")
print(type(a))
print(type(b))
print(type(c))
print()

'''
Integers can be of different number systems:
1. Decimal (primarily used)
2. Binary 
3. Octal
4. Hexademical
'''
a1 = 45 #decimal
a2 = 0b101101 # 45 in binary, 
a3 = 0o55 #45 in octal
a4 = 0x2D # 45 in hexadecimal
print("NUMBER SYSTEMS: ")
print(a1)
print(a2)
print(a3)
print(a4)
print()

'''
NUMBER SYSTEM CONVERSION:
Decimal numbers can be converted to binary, octal or hexadecimal using bin(), oct() and hex() functions respectively
'''
print("NUMBER SYSTEM CONVERSION: ")
print(bin(a1))
print(oct(a1))
print(hex(a1))
print()

'''
Floats are real numbers, both negative and positive with fractions usually distinguised by ' . '
It also supports scientific notation.
'''
print("FLOATS: ")
b1 = 873.99488221
b2 = -232.12
b3 = 4.2232232e4 # which is 42232.232
print(b1)
print(b2)
print(b3)
print()

'''
Numbers support arithmetic operations also: 
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus : returns remainder of division operation
6. Exponent
7. Floor Division: rounds the result of the division to the nearest integer

These operations can be performed amongst numbers directly or numbers stored in some variable.
'''
d1 = 44 + 90
d2 = 5 - 2
d3 = d1 * d2
d4 = 16 / d2
d5 = 91 % 10
d6 = 4 ** 3
d7 = 16 // d2
print("ARITHMETIC OPERATIONS: ")
print(d1)
print(d2)
print(d3)
print(d4)
print(d5)
print(d6)
print(d7)
print()

'''
Commonly used functions on Numbers:
1. pow(x,y)    : returns x raised to the y power
2. abs(x)      : returns the absolute value of a number
3.round(x,y)   : returns x rounded to a precision of y after decimal point
4.is_integer() : returns True if number has no fractional part/reminder. Useful for quick input validation.
'''
print("COMMMONLY USED FUNCTIONS: ")
print(pow(10,4))
print(abs(24))
print(abs(-24))
print(round(6282.37889749874988, 3))

num = 31.0
num1 = 31.9
print(num.is_integer())
print(num1.is_integer())

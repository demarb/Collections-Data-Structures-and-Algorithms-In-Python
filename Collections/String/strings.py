'''
Strings in Python are sequence of characters surrounded by double, single or even triple quotations.
However a character is not a defined data type in Python, instead it is a string with length of 1.
'''

print("STRINGS:")
a = "Hello Mark"
b = ' and Jenna.'
greetings= '''Dear
Sir
or Madam
'''
print(a) #Hello Mark
print(b) # and Jenna.
print(greetings)
print()

'''
String Operations
1. '+' operator
2. '*' operator
3. 'in' operator 
Strings can be joined together using '+', we call this concatenation
Strings can be multiplied to give multiple copies using '*'
The 'in' operator returns True/False on checking if a string is a sub string of another string. Can be negated by placing not before in.
'''
print("STRING OPERATIONS: ")
print(a + b) #Hello Mark and Jenna.
print(a + b + " Thank you for coming") #Hello Mark and Jenna. Thank you for coming

print(a * 3) #Hello MarkHello MarkHello Mark

c = 'and'
print(c in b) #True
print("Pello" in a) #False

print()

'''
Accessing String Elements
1. Accessing certain position : using index starting at 0 for first character
2. Looping through strings
'''
print("ACCESSING STRING ELEMENTS:")
address = "192 Harbour Avenue, Kingston 23"
print(address[4]) #H

#lets try to change the character at index 4 and see and what happens
# address[4] = "h" 
    #TypeError: 'str' object does not support item assignment
    #Strings  are immutable in Python. This means you cannot change it in place.

#Looping
for letter in address:
    print(letter)
    
#We can also use this to solve our changing a character in our string by copying into another variable instead.
#Consider the following.

new_address = ""
    
for letter in address:
    if letter == "H":
        new_address+= "h"
    else:
        new_address+= letter

print(new_address) #192 harbour Avenue, Kingston 23
print()

'''
String Methods:
1. len() : Checks the length of a string
2. ord() : Returns ascii value of a character
3. str() : Returns string version of a object
4. capitalize() : Converts the first character of a string to upper case
5. upper() and lower() : Converts entire string to uppercase and lowercase respectively

There are several others also.
'''
print("STRING METHODS:")
print(len(new_address)) #31
print(ord("r")) #114
print(str(43)) #"43"
print('hi there'.capitalize()) #Hi there
print(new_address.upper()) #192 HARBOUR AVENUE, KINGSTON 23
print("PILLOW".lower()) #pillow
print()

'''
SLICING VS SPLITING
Slicing : returns a range of characters in a string given certain indexes
Spliting : returns a list where each list items are those in the original found between the seperator passed to the split() function.
'''

# Slicing
text = "Hello fellow programmer"
print("SPLITTING AND SLICING: ")
print(text[:4]) #Hell
print(text[3:]) #lo fellow programmer
print(text[3:9]) #lo fel
#Reverse indexing
print(text[-9:-3]) #rogram


#Splitting
print(text.split("e")) #['H', 'llo f', 'llow programm', 'r']
print(text.split()) #['Hello', 'fellow', 'programmer']
print()
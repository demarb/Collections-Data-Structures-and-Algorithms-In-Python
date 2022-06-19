'''
Tuples are indexed, ordered collections similar to list that store multiple values as a single variable. 
Tuples differ from list though in that they are unchangeable (immutable) and are declared with round brackets instead of square brackets.

'''

'''
DECLARING TUPLES
1. Rounded brackets
2. Tuple()

If you only have one item inside the tuple, the first item must be followed by a comma for it to be a valid tuple declaration
'''
print("DECLARING TUPLES")

brands = ("Nike", "Gucci", "Balenciaga", "Calvin Klein")
print(brands) # ('Nike', 'Gucci', 'Balenciaga', 'Calvin Klein')
movies = ("Iron Man",)
print(movies) # ('Iron Man',)
user_rating = tuple(("mike_334", True, "Sonic", 7.5))
print(user_rating) # ('mike_334', True, 'Sonic', 7.5)

print() 

'''
UPDATING TUPLES
Tuples are immutable so to make changes to them, we need to convert 
them to lists by passing them to the list() constructor. We make changes to the list then we can 
convert them back into tuples using tuple().
'''
print("UPDATING TUPLES")

x = (1, 2, 3, 4, 5)
print(x) # (1, 2, 3, 4, 5)

numbersList= list(x)
print(numbersList) #[1, 2, 3, 4, 5]

numbersList.append(99)
print(numbersList) # [1, 2, 3, 4, 5, 99]
numbersList.pop(2)
print(numbersList) # [1, 2, 4, 5, 99]

x = tuple(numbersList)
print(x) # (1, 2, 4, 5, 99)

print()

'''
PACKING AND UNPACKING TUPLES
When we assign values to a tuple, its called packing.
The reverse can be done, where we assign the values in a tuple to individual variables. We call this unpacking.

When unpacking tuples we can either unpack all the values to inviduals variables or unpack some to variables and the remaining to a seperate lists
'''

print("PACKING AND UNPACKING TUPLES")
studentAge = (14, 16, 13)
print(studentAge) # (14, 16, 13)

print("]tUnpacking to individual variables")
(markAge, matthewAge, jennaAge) = studentAge
print(markAge) #14
print(matthewAge) #16
print(jennaAge) #13

print("\tUnpacking to individual variables and lists")
(maleAge, *femaleAge) = studentAge
print(maleAge) #14
print(femaleAge) #[16, 13]

print()

'''
LOOPING THROUGH TUPLES
1. For loops
2. While loops

'''
print("LOOPING THROUGH TUPLES")
phoneBrands = ("Samsung", "Apple", "Hyunai", "LG", "Blackberry")
print(phoneBrands) #('Samsung', 'Apple', 'Hyunai', 'LG', 'Blackberry')

print("\tFor-loops")
for phone in phoneBrands:
    print(phone)
    '''
    Samsung
    Apple
    Hyunai
    LG
    Blackberry
    '''
    
print("\tFor-loops - with index")
for phone in range(len(phoneBrands)):
    print(phoneBrands[phone])
    '''
    Samsung
    Apple
    Hyunai
    LG
    Blackberry
    '''

print("\tWhile-loops")
phoneCnt= 0
while phoneCnt < len(phoneBrands):
    print(phoneBrands[phoneCnt])
    phoneCnt = phoneCnt + 1

    '''
    Samsung
    Apple
    Hyunai
    LG
    Blackberry
    '''
    
print()
'''
TUPLE METHODS
1. Count - returns the number of times a value appears in a tuple
2. Index - finds the index of a specified item
'''

print("TUPLE METHODS")
phoneBrands2 = ("Samsung", "LG", "Apple", "Hyunai", "LG", "Blackberry")
print(phoneBrands2) #('Samsung', 'LG', 'Apple', 'Hyunai', 'LG', 'Blackberry')

print("\tcount() Method")
print(phoneBrands2.count("LG")) #2

print("\tindex() Method")
print(phoneBrands2.index("Hyunai")) #3

print()
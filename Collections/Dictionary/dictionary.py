'''
Dictionaries are ordered (unordered in early versions of Python),
mutable collections in Python that store data in Key:value pairs.
'''

'''
DECLARING DICTIONARIES
1. Curly brackets
2. dict() constructor

Note: In declaring dictionaries, the keys must be immutable (string, number, tuple) and unique. The values can be duplicated for different keys
'''
print("DECLARING DICTIONARIES")
#Declaring an empty dictionary
emptyDict = {}

#Declaring dictionary using {}
houseDict = {
    'numBedrooms': 3,
    'rented': 'Yes',
    'occupants': ['John', 'Mary', 'Max']
}
print(houseDict)
#{'numBedrooms': 3, 'rented': 'Yes', 'occupants': ['John', 'Mary', 'Max']} 

#Declaring dictionary using dict()
students = dict([(1,'Goseph'), ((2, 'Two'), 'Brittany')])
# Note the use of , instead of :

print(students) # {1: 'Goseph', (2, 'Two'): 'Brittany'}

print()

'''
ACCESSING DICTIONARIES
1. keys(): returns a list of all keys of a given dictionary.
2. get(): returns the value of a given key in a dictionary, and returns None if the key does not exist.
3. Square Brackets []: returns the value of a given key in a dictionary, and raises a KeyError if the key does not exist..
4. values(): returns a list of all values of a given dictionary.
5. items(): returns all key:value pairs as a tuple in a list
'''
print("ACCESSING DICTIONARIES")

print("\t.keys() - method ")
print(houseDict.keys()) #dict_keys(['numBedrooms', 'rented', 'occupants'])

print("\t.get() method")
print(houseDict.get('numBedrooms')) #3
print(houseDict.get('numKitchens')) #None

print("\t[] - method")
print(houseDict['rented']) #Yes
# print(houseDict['landlord']) #KeyError: 'landlord'

print("\t.values() - method ")
print(houseDict.values()) #dict_values([3, 'Yes', ['John', 'Mary', 'Max']])

print("\t.items() - method ")
print(houseDict.items()) 
#dict_items([('numBedrooms', 3), ('rented', 'Yes'), ('occupants', ['John', 'Mary', 'Max'])])

print()

'''
CHANGING, ADDING AND REMOVING ITEMS FROM DICTIONARIES
1. Changing Values of Keys using [] and Python assignment
2. Adding New Items to Dictionary using [] with new keys and Python assignment
3. Removing items from dictionary using pop() which accepts a key as an argument
4. Removing items from dictionary using popitem() which removes the last inserted item in Python 3.7 and beyond.
5. Removing all items from the dictionary using clear()
'''
print("CHANGING, ADDING AND REMOVING ITEMS FROM DICTIONARIES")
petNames={
    1: 'Spots',
    2: 'Cupcake',
    3: 'Max',
    4: 'Ben',
}

print("\tChanging Values of Keys using [] and Python assignment")
petNames[2] = 'Shuckles'
print(petNames)
#{1: 'Spots', 2: 'Shuckles', 3: 'Max', 4: 'Ben'}

print("\tAdding New Items to Dictionary using [] with new keys and Python assignment")
petNames[5] = 'Dupri'
print(petNames)
#{1: 'Spots', 2: 'Shuckles', 3: 'Max', 4: 'Ben', 5: 'Dupri'}

print("\tRemoving items from dictionary using pop() which accepts a key as an argument")
petNames.pop(3)
print(petNames)
#{1: 'Spots', 2: 'Shuckles', 4: 'Ben', 5: 'Dupri'}

print("\tRemoving items from dictionary using popitem() which removes the last inserted item in Python 3.7 and beyond.")
petNames.popitem()
print(petNames)
#{1: 'Spots', 2: 'Shuckles', 4: 'Ben'}

print("\tRemoving all items from the dictionary using clear()")
petNames.clear()
print(petNames) #{}

print()

'''
NB: Nested Dictionaries exist. Dictionaries can have dictionaries within them.

'''
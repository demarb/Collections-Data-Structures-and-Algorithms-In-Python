'''
Lists are ordered collections of objects; meaning they can store multiple pieces of data, of varying types in a single variable.
By ordered, we mean that the list has a distinctive order (set of index) at creation that cannot change. The fact that lists are order therefore,
means that we can have duplicate values inside in our lists.
Unlike numbers and strings, lists are mutable.

They are created in two ways:
    1. Square brackets
    2. List() constructor    
    
Many of the things we did with strings are also allowed with lists such as indexing, reverse indexing, checking the length of lists with len(),
slicing lists and using the in operator to check if the item is in the list. Note also, that lists can lists (nested lists)

'''
statesList = ["Florida", "New York", "California", "Florida"]
carsList = list(("Toyota", "Audi", "BMW", "Mistubishi"))

print("LISTS: ")
print(statesList[1]) #New York
print(statesList[-1]) #Florida
print(len(statesList)) #4
print(carsList[1:3]) #['Audi', 'BMW']
print("Audi" in carsList) #True
print()


'''
Modifing Lists
1. Changing value of list item
2. Appending to list : adding a list item to end of list
3. Inserting new items to the list at specific position.
4. Extending lists
5. Removing list items with remove, pop, del and clear
6. Deleting a list from memory

'''

#1. Changing value of list item
print("CHANGING LISTS ITEMS")
statesList[0] = "Hawaii"
print(statesList) #['Hawaii', 'New York', 'California', 'Florida']
print()

#2. Appending list items
print("APPENDING LISTS ITEMS")
statesList.append("Connecticut") 
print(statesList) #['Hawaii', 'New York', 'California', 'Florida', 'Connecticut']
print()

#3. Inserting list items at specific index
print("INSERTING LISTS ITEMS")
statesList.insert(2, "New Jersey")
print(statesList) #['Hawaii', 'New York', 'New Jersey', 'California', 'Florida', 'Connecticut']
print()

#4. Extending one list to another
print("EXTENDING LISTS")
statesList.extend(carsList)
print(statesList) #['Hawaii', 'New York', 'New Jersey', 'California', 'Florida', 'Connecticut', 'Toyota', 'Audi', 'BMW', 'Mistubishi']
print()

#5. Removing list items with remove, pop, clear and del
print("REMOVE, POP, CLEAR & DEL")

#remove : deletes the specified item from list
print("\tRemove")
print(carsList) #['Toyota', 'Audi', 'BMW', 'Mistubishi']
carsList.remove("BMW")
print(carsList) # ['Toyota', 'Audi', 'Mistubishi']

#pop : deletes the item at specified index
print("\tPop")
print(carsList) # ['Toyota', 'Audi', 'Mistubishi']
carsList.pop(2)
print(carsList) # ['Toyota', 'Audi']

# del : deltete the item at position specified or deletes an entire list
print("\tDel at index")
print(carsList) # ['Toyota', 'Audi']
del carsList[0]
print(carsList) # ['Audi']

print("\tDel list from memory")
print(carsList) # ['Audi']
del carsList
#print(carsList) # NameError: name 'carsList' is not defined

#clear : empties a list bt it remains in memory
print("\tClear")
print(statesList) #['Hawaii', 'New York', 'New Jersey', 'California', 'Florida', 'Connecticut', 'Toyota', 'Audi', 'BMW', 'Mistubishi']
statesList.clear()
print(statesList) # []

print()


'''
List Unpacking
1. In scenario 1 the length of the list we are unpacking 
must match the number of variables we are assigning it to

2. With scenerio 2, we can unpack a list and place the
remaining values (packing) in a new list using *
'''
print("LIST UNPACKING")
print("Scenario 1:")
numbers = [1,2,3]
first, second, third = numbers
print(first) # 1
print(second) # 2
print(third) # 3

print("Scenario 2:")
numbers = [1,2,3,7,6,5,4,4,6,7,5,3,5,6,]
first, second, *remainingNums = numbers
print(first) # 1
print(second) # 2
print(remainingNums) #[3, 7, 6, 5, 4, 4, 6, 7, 5, 3, 5, 6]

'''
Looping through lists. Lists are iterable
1. for loop
2. for loop with enumerable() to get index as well. Returns a tuple
'''
subjects = ["Math", "Science", "Arts", "English", "Geography"]

for subject in subjects:
    print(subject)
    '''
    Math
    Science
    Arts
    English
    Geography
    '''
    
    
for subject in enumerate(subjects):
    print(subject)
    '''
    (0, 'Math')
    (1, 'Science')
    (2, 'Arts')
    (3, 'English')
    (4, 'Geography')
    '''
    # NOTEBRIEFLY: We could unpack the tuple at subject 
    # eg. for inx, subject in enumerate(subjects):

print()

'''
Copying and Sorting Lists
'''
print("COPYING AND SORTING LISTS")

print("Copying Lists")
subjectsCopy = subjects.copy()
print(subjectsCopy) # ['Math', 'Science', 'Arts', 'English', 'Geography']

print("Sorting Lists")
print(numbers) #[1, 2, 3, 7, 6, 5, 4, 4, 6, 7, 5, 3, 5, 6]
numbers.sort()
print(numbers) # [1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7]
print(subjectsCopy) # ['Math', 'Science', 'Arts', 'English', 'Geography']
subjectsCopy.sort()
print(subjectsCopy) # ['Arts', 'English', 'Geography', 'Math', 'Science']

print() 


'''
LIST COMPREHENSION
A shortcut method for creating a new list from an existing list often using some condition.

Syntax :
    newlist = [expression for item in iterable if condition == True]
    --        [add this to the list FOR each of this IN original list IF some condition is met]
eg. Lets say we have a list with european country names.
And we want a new list with European countries with an 'e' in their names,
we could do this two ways.
1. using a traditional loop with if statement
2. using list comprehension which encompasses both the loop and if statement in one line of code

'''

euroCountries = ['France', 'United Kingdom', 'Spain', 'Germany', 'Hungrary', 'Belgium', 'Italy', 'Sweden', 'Ukraine']
print(euroCountries) #['France', 'United Kingdom', 'Spain', 'Germany', 'Hungrary', 'Belgium', 'Italy', 'Sweden', 'Ukraine']

eCountriesMethod1 = []
for country in euroCountries:
    if "e" in country:
        eCountriesMethod1.append(country)
        

print(eCountriesMethod1) #['France', 'United Kingdom', 'Germany', 'Belgium', 'Sweden', 'Ukraine']

eCountriesMethod2A = [country for country in euroCountries if "e" in country]
print(eCountriesMethod2A) #['France', 'United Kingdom', 'Germany', 'Belgium', 'Sweden', 'Ukraine']
eCountriesMethod2B = [country.upper() for country in euroCountries if "e" in country]
print(eCountriesMethod2B) #['FRANCE', 'UNITED KINGDOM', 'GERMANY', 'BELGIUM', 'SWEDEN', 'UKRAINE']
eCountriesMethod2C = ["Country found" for country in euroCountries if "e" in country]
print(eCountriesMethod2C) #['Country found', 'Country found', 'Country found', 'Country found', 'Country found', 'Country found']
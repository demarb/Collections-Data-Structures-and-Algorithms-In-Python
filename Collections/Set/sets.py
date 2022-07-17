'''
Sets are unordered unindexed collections in Python. The items in a set themselves cannot be changed (they are immutable),
however, the set as a whole is mutable(you can add and remove items from it). Furthermore, the items in a set should be unique
'''

'''
DECLARING SETS
1. Curly brackets
2. Set() constructor

Note: in declaring sets, the set items can be the same data type or multiple types. Additionally, set items cannot be mutable
(lists, dictionaries,sets)
'''
print("DECLARING SETS")

vegetables = {"carrot", "onion", "eskellion"}
student1Grades = {"Math", 86, 64, (90, 34, 23)}
subjects = set(("English", "Literature", "Geography", "Spanish", "Geography"))

print(vegetables) # {'carrot', 'onion', 'eskellion'}
print(student1Grades) # {64, (90, 34, 23), 86, 'Math'}
print(subjects) # {'English', 'Geography', 'Literature', 'Spanish'}

print()

'''
DECLARING EMPTY SETS
If we try to declare an empty set using {}, in Python we will get  a dictionary.
Therefore, we must use the set constructor without any arguments.

'''
print("DECLARING EMPTY SETS")

namesA = {}
print(type(namesA)) # <class 'dict'>

namesB = set()
print(type(namesB)) # <class 'set'>
#check length of set namesB
print(len(namesB)) # 0

print()

'''
MODIFYING SETS
Note: Since sets are unordered, we cannot use index and slicing to access elements

We can add and delete elements from a set using a number of methods:
1. add(): adds a single set item
2. update(): adds multiple set items from an iterable
3. remove(): deletes a set item however, the item must be a members or else an error is thrown
4. discard(): deletes a set item but does not produce an error if the item is not a member of the set.
5. pop(): deletes a random element of the set, since sets are unordered.
6. clear(): deletes all the elements in a set.
7. del: removes a set from memory

'''
print("MODIFYING SETS")
primeNumbers = {1,3}
print(primeNumbers) # {1, 3}

print("\tAdding elements with - add()")
primeNumbers.add(5)
print(primeNumbers) # {1, 3, 5}

print("\tAdding elements with - update() which accepts one or more iterable")
primeNumbers.update([7,11,7])
print(primeNumbers) # {1, 3, 5, 7, 11}
primeNumbers.update([13, 17], (19,23)) # Note: We could add another set using update() also.
print(primeNumbers) # {1, 3, 5, 7, 11, 13, 17, 19, 23}

print("\tDeleting elements with - remove()")
#With remove(), the element must be a member else a KeyError is produced
primeNumbers.remove(3)
#primeNumbers.remove(44) # KeyError: 44
print(primeNumbers) # {1, 5, 7, 11, 13, 17, 19, 23}

print("\tDeleting elements with - discard()")
#With discard(), the element must be a member else a KeyError is produced
primeNumbers.discard(11)
primeNumbers.discard(44)
print(primeNumbers) # {1, 5, 7, 13, 17, 19, 23}

print("\tDeleting elements with - pop()")
primeNumbers.pop()
print(primeNumbers) # {5, 7, 13, 17, 19, 23}

print("\tDeleting elements with - clear()")
primeNumbers.clear()
print(primeNumbers) # set()

print("\tDeleting the set with - del")
del primeNumbers
# print(primeNumbers) # NameError: name 'primeNumbers' is not defined

print()

'''
SET OPERATIONS
1. Union
2. Intersection
3. Set Difference
4. Symmetric Difference


'''
print("SET OPERATIONS")
setA = {10, 20, 30, 40}
setB = {30, 40, 50, 60}

print("\tUnion")
#The set of all elements from two sets. There are two ways to do this.
print(setA.union(setB)) # {40, 10, 50, 20, 60, 30}
print(setA | setB) # {40, 10, 50, 20, 60, 30}

print("\tIntersection")
#The set of all elements common to two sets. There are two ways to do this.
print(setA.intersection(setB)) # {40, 30}
print(setA & setB) # {40, 30}

print("\tSet Difference")
#The set of elements of a given set that is not found in the other set. There are two ways to do this.
print(setA.difference(setB)) # {10, 20}
print(setA - setB) # {10, 20}

print("\tSymmetric Difference")
#The set of all elements of two sets excluding elements that intersect from both. There are two ways to do this.
print(setA.symmetric_difference(setB)) # {10, 50, 20, 60}
print(setA ^ setB) # {10, 50, 20, 60}

'''
OTHER SET METHODS YOU  MAY WANT TO LOOK AT:
1. difference_update(): Removes all elements of another set from this set
2. intersection_update(): Updates the current set with the intersection of itself and another
3. symmetric_difference_update(): Updates the current set with the symmetric difference of itself and another
4. issubset(): Returns whether another set contains this set or not
5. isdisjoint(): Returns True if two sets do not have an intersection
6. issuperset(): Returns whether this set contains another set.
7. copy(): Returns a copy of the set


'''
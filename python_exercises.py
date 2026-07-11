"""
-To declare variable, you need a variable name followed by =
then the value of the variable.
-It can be a string, integer/float, boolean. etc.
"""

from collections.abc import Set


string = 'Jay'
integer = 22
float = 22.5
boolean = True

"""
-Can only start with a letter or underscore, no numbers
-Names can only have a-z, A-Z, 0-9, and underscores
-Variable names are case sensitive so age and Age and AGE are 
unique variable names.
-Names cannot be a python reserved names like if, class, def
"""

"""
Comments are used to leave notes to your code
-Single line comment using #
-Multi line comment using """  """
"""

"""
You can use print() to print the value of a variable to the
console
"""

print('Hello, World!')
print(string)
print(integer)
print(float)
print(boolean)

"""
Python is a dynamically typed language, meaning you do not
have to declare the type of variable when creating it.
The interpreter will determine the type of variable based
on the value assigned to it.
"""

#Integer is a number without a decimal point
age = 22
print('Age:', age) # = Age: 22

#Float is a number with a decimal point.
height = 5.9
print('Height:', height) # = Height: 5.9

#String is a sequence of characters enclosed in quotes.
name = 'Jay'
print('Name:', name) # = Name: Jay

#Boolean is a data type that can only beTrue or False.
is_student = True
print('Is Student:', is_student) # = Is Student: True

#Set is an unordered collection of unique elements.
numbers = {1, 2, 3, 4, 5}
print('Numbers:', numbers) # = Numbers: {1, 2, 3, 4, 5}

#Dictionary is a collection of key-value pairs, in curly braces.
person = {'name': name, 'age': age, 'height': height}
print('Person:', person) # = Person: {'name': 'Jay', 'age': 22, 'height': 5.9}

#Tuple is an IMMUTABLE ordered collection, in parentheses.
coordinates = (10, 20)
print('Coordinates:', coordinates) # = Coordinates: (10, 20)

#Range is a sequence of numbers, often used in for loops.
range_A = range(5)
#Note:Last number is exclusive starting from 0
print('Range A:', range_A) # = Range A: range(0, 5)
print('Range A:', list(range_A)) # = Range A: [0, 1, 2, 3, 4]

range_B = range(1, 6)
#Note:Last number is exclusive
print('Range B:', range_B) # = Range B: range(1, 6) 
print('Range B:', list(range_B)) # = Range B: [1, 2, 3, 4, 5]

#List is an ordered collection of elements, in square brackets.
fruits = ['apple', 'banana', 'cherry']
print('Fruits:', fruits) # = Fruits: ['apple', 'banana', 'cherry']

#None is a special data type that represents the absence of a value.
value = None
print('Value:', value) # = Value: None
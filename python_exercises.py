"""
-To declare variable, you need a variable name followed by =
then the value of the variable.
-It can be a string, integer/float, boolean. etc.
"""

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

"""
Immutable Types: An immutable object stays the same after
it's created. If you "change" it, Python actually creates a
new object instead.
"""
name = 'Jay'
name = 'Chris' #Jay is still there but Chris overlaps it.

print('Name:', name) # = Name: Chris

"""
Mutable Types: These types can change once declared. You can
add, remove, or update their items. They include collection
types such as list, set, and dictionary.
"""
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange') #Add an item to the end of the list.

print('Fruits:', fruits) # = Fruits: ['apple', 'banana', 'cherry', 'orange']

#type() function is used to check the data type of a variable.
food = 'Pizza'
pieces = 8
print(type(food)) # = <class 'str'>
print(type(pieces)) # = <class 'int'>

#isinstance() function is used to check if a variable is an instance of a specific data type.
print(isinstance(food, str)) # = True
print(isinstance(pieces, int)) # = True

#Accessing Characters from a String
#You can access individual characters in a string using indexing.
message = "Hello, World!"
print(message[0])  # Output: H
print(message[7])  # Output: W

print(message[-1]) # Output: !
print(message[-5]) # Output: o

#Escaping Characters in a String
#You can use the backslash (\) to escape characters in a string.
text = "He said, \"Hello, World!\""
print(text)  # Output: He said, "Hello, World!"

#String Concatenation
#You can concatenate strings using the + operator.
frst_name = "Jay"
last_name = "Sese"
full_name = frst_name + " " + last_name
print(full_name)  # Output: Jay Sese

#You can perform concatenation and assignment in the same step.
introduction = "Hello, my name is "
introduction += full_name
print(introduction)  # Output: Hello, my name is Jay Sese

#f-Strings (Formatted String Literals)
#You can use f-strings to embed expressions inside string literals.
intro = f"Hello, my name is {full_name} and I am {age} years old."
print(intro)  # Output: Hello, my name is Jay Sese and I am 22 years old.

"""
String Slicing

You can extract a substring from a string using slicing.

str[start:stop:step]
Start: The starting index of the substring (inclusive).
Stop: The ending index of the substring (exclusive).
Step: The step size for slicing (optional).
"""
message = 'Python is fun!'

print(message[0:6])  # Python
print(message[7:])  # is fun!
print(message[::2])  # Pto sfn

#Getting the Length of a String
#You can use the len() function to get the length of a string.
text = "Hello, World!"
print(len(text))  # Output: 13
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

print('---------------------------------------')

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

slicing = 'Trying Slicing'
print(slicing[0:3]) #  Output: Try
#The first index is zero meaning Letter T is on index 0
#The second index is 3 meaning Letter y is on index 2
#In second index, the letter on that index is not included

print(slicing[7:13])  # Output: Slicing
#Index 7 is the letter S
#Index 13 is after the letter g, so it is not included in the output.
#You can leave the second index empty to slice until the end of the string.

print(slicing[7:])  # Output: Slicing
#Even without the second index, it will slice until the end of the string.

print(slicing[:6])  # Output: Trying
#You can leave the first index empty to slice from the beginning of the string.

print(slicing[::2])  # Output: Tyn lcn
"""
The step size is 2, so it takes every second character from the string.

T r y i n g   S l i c i n g
0 1 2 3 4 5 6 7 8 9 10 11 12 13

Stepping through the string with a step size of 2, we get:
Index 0: T
Index 2: y
Index 4: n
Index 6:  
Index 8: l
Index 10: c
Index 12: n
"""

print('---------------------------------------')

#Getting the Length of a String
#You can use the len() function to get the length of a string.
text = 'Hello, World!'
print(len(text))  # Output: 13

#Working with the in operator
#in Operator returns a boolean value (True or False) based on whether a substring exists within a string.
print('Hello' in text)  # Output: True
print('Python' in text)  # Output: False
print('Python' not in text)  # Output: True
print('World' not in text)  # Output: False

print('Hotdog' in text)  # Output: False
print('Hotdog' not in text)  # Output: True

print('---------------------------------------')

#Common String Methods
#str.upper() returns a new string with all characters converted to uppercase.
print(text.upper())  # Output: HELLO, WORLD!

#str.isupper() returns True if all characters in the string are uppercase, otherwise False.
print(text.isupper())  # Output: False
upper_text = text.upper()
print(upper_text.isupper())  # Output: True

#str.lower() returns a new string with all characters converted to lowercase.
print(text.lower())  # Output: hello, world!

#str.islower() returns True if all characters in the string are lowercase, otherwise False.
print(text.islower())  # Output: False
lower_text = text.lower()
print(lower_text.islower())  # Output: True

print('--------------------------------------')

#str.strip() returns a new string with leading and trailing whitespace removed.
willstrip = '   Hello, World!   '
stripped = willstrip.strip()
print(stripped)  # Output: Hello, World! from '   Hello, World!   '

#replace() returns a new string with all occurrences of a substring replaced with another substring.
replaced_text = text.replace('World', 'Python')
print(replaced_text)  # Output: Hello, Python!

hi_python = replaced_text.replace('Hello', ' Hi')
print(hi_python)  # Output:  Hi, Python!

#split() returns a list of substrings by splitting the string at the specified delimiter.
split_text = 'I-will-split-this-string'
split_list = split_text.split('-')
print(split_list)  # Output: ['I', 'will', 'split', 'this', 'string']

split_slash = 'I/will/split/this/string'
split_slash_list = split_slash.split('/')
print(split_slash_list)  # Output: ['I', 'will', 'split', 'this', 'string']

#join() returns a new string by joining the elements of an iterable (like a list) with a specified delimiter.
will_join = ['I', 'will', 'join', 'this', 'list']
joined_string = ' '.join(will_join)
print(joined_string)  # Output: I will join this list

slash_join = ['I', 'will', 'join', 'this', 'list']
joined_slash_string = '/'.join(slash_join) 
print(joined_slash_string)  # Output: I/will/join/this/list

dash_join = ['I', 'will', 'join', 'this', 'list']
joined_dash_string = '-'.join(dash_join)
print(joined_dash_string)  # Output: I-will-join-this-list

#str.startswith() returns True if the string starts with the specified prefix, otherwise False.
print(text.startswith('Hello'))  # Output: True
print(text.startswith('Hi'))  # Output: False

print(text.startswith('H'))  # Output: True

#str.endswith() returns True if the string ends with the specified suffix, otherwise False.
print(text.endswith('World!'))  # Output: True
print(text.endswith('Python!'))  # Output: False

print(text.endswith('!')) # Output: True

"""
str.find() 

It finds the first occurrence of the substring and returns its index.
If the substring is not found, it returns -1.

H e l l o ,   W o r l d !
0 1 2 3 4 5 6 7 8 9 10 11 12
The substring 'World' starts at index 7 in the string 'Hello, World!'.
"""
print(text.find('World'))  # Output: 7
print(text.find('Python'))  # Output: -1: Meaning not found

print(text.find('!'))  # Output: 12: The first occurrence of '!' is at index 12

#str.count() returns the number of occurrences of a substring in the string.
count_text = 'Hello, World! Hello, Python!'
print(count_text.count('Hello'))  # Output: 2
print(count_text.count('World'))  # Output: 1
print(count_text.count('Python'))  # Output: 1
print(count_text.count('Java'))  # Output: 0: Meaning not found
print(count_text.count('!'))  # Output: 2: The substring '!' appears twice in the string.
print(count_text.count('l'))  # Output: 5: The substring 'l' appears five times in the string.

#str.capitalize() returns a new string with the first character capitalized and the rest lowercased.
capitalize_text = 'hello, world!'
print(capitalize_text.capitalize())  # Output: Hello, world!

#str.title() returns a new string with the first character of each word capitalized.
title_text = 'hello, world! welcome to python.'
print(title_text.title())  # Output: Hello, World! Welcome To Python.

#str.isalpha() returns True if all characters in the string are alphabetic and there is at least one character, otherwise False.
alpha_text = 'HelloWorld'
print(alpha_text.isalpha())  # Output: True
non_alpha_text = 'Hello World'
print(non_alpha_text.isalpha())  # Output: False: Because of the space character
numeric_text = '12345'
print(numeric_text.isalpha())  # Output: False: Because of the numbers

#str.isdigit() returns True if all characters in the string are digits and there is at least one character, otherwise False.
digit_text = '12345'
print(digit_text.isdigit())  # Output: True
non_digit_text = '12345abc'
print(non_digit_text.isdigit())  # Output: False: Because of the letters

#str.maketrans() and str.translate() are used together to replace characters in a string based on a translation table.
translation_table = str.maketrans('aeiou', '12345')
print(translation_table)  # Output: {97: 49, 101: 50, 105: 51, 111: 52, 117: 53}

tresult = 'aeiou'.translate(translation_table)
print(tresult)  # Output: 12345

table = str.maketrans('abc', '123')
translated = 'abcabc'.translate(table)
print(translated)  # Output: 123123

print('--------------------------------------')

int1 = 12
int2 = 25
float1 = 0.3
float2 = 1.2

#Addition (+) adds two numbers together.
print('Integer Addition: ', int1 + int2)  # Output: 37
print('Float Addition: ', float1 + float2)  # Output: 1.5

#Subtraction (-) subtracts the second number from the first.
print('Integer Subtraction: ', int2 - int1)  # Output: 13
print('Float Subtraction: ', float2 - float1)  # Output: 0.8999999999999999

#Multiplication (*) multiplies two numbers together.
print('Integer Multiplication: ', int1 * int2)  # Output: 300
print('Float Multiplication: ', float1 * float2)  # Output: 0.36

#Division (/) divides the first number by the second and returns a float.
print('Integer Division: ', int2 / int1)  # Output: 2.0833333333333335
print('Float Division: ', float2 / float1)  # Output: 4.0

#When you add a float and an integer, the result will be converted to a float like this:
print(int1 + int2 + float1 + float2)  # Output: 38.5

#Modulo Operator (%) returns the remainder of a division operation.
print('Integer Modulo: ', int2 % int1)  # Output: 1

"""
25 divided by 12 is 2 with a remainder of 1, so the result of 25 % 12 is 1.
The modulo operator is often used to determine if a number is even or odd.
"""

#Floor Division (//) divides the first number by the second and returns the largest integer less than or equal to the result.
print('Integer Floor Division: ', int2 // int1)  # Output: 2

"""
25 divided by 12 is 2.0833333333333335, and the largest integer less than or equal to 2.0833333333333335 is 2, so the result of 25 // 12 is 2.
The floor division operator is often used to perform integer division.
"""

#Exponentiation Operator (**) raises the first number to the power of the second number.
print('Integer Exponentiation: ', int1 ** 2)  # Output: 144

"""
12 raised to the power of 2 is 144, so the result of 12 ** 2 is 144.
The exponentiation operator is often used to perform mathematical calculations involving powers.    
"""

del float  
# Float() function converts an integer to float.
int3 = 2003
float_int3 = float(int3)
print(float_int3)  # Output: 2003.0

#Int()  function converts a flat to an interger.
print(int(float2))  # Output: 1

#Round() function rounds a float to the nearest integer.
print(round(float2))  # Output: 1

#Abs() function returns the absolute value of a number.
print(abs(int1))  # Output: 12

#Pow() function raises a number to the power of another.
power = pow(2,5)
print(power) # Output : 32

"""
2 times 2, 4
4 times 2, 8
8 times 2, 16
16 times 2, 32
"""

"""
Augmented Assignments
Combines a binary operation in one step. It takes a variable,
applies an operation to it with another value, and stores
the result back into the same variable.
"""

#Addition assignment
aug_add = 1
aug_add += 11
print(aug_add) #12

#Subtraction assignment
aug_sub = 25
aug_sub -= 13
print(aug_sub) #12

#Multiplication assignment
aug_multi = 3
aug_multi *= 4
print(aug_multi) #12

#Division assignment
aug_div = 25
aug_div /= 5
print(aug_div) #5.0

#Floor Division assignment
aug_floor = 25
aug_floor //= 12
print(aug_floor) #2
 
"""
25 divided by 12 is 2.0833333333333335, and the largest
integer less than or equal to 2.0833333333333335 is 2, so
the result of 25 // 12 is 2. The floor division operator is 
often used to perform integer division.
"""

#Modulo assignment
aug_mod = 25
aug_mod %= 4
print(aug_mod) #1

"""
25 divided by 4 is 6 with a remainder of 1, so the result
of 25 % 4 is 1. The modulo operator is often used to
determine if a number is even or odd.
"""

#Exponentiation assignment
aug_exp = 5
aug_exp **= 3
print(aug_exp) #12

"""
There are other augmented assignment operators too
like those for bitwise operators.
They include &=, ^=, >>=, and <<=.
"""

"""
Working with Function
Functions are reusable pieces of code that take
inputs(arguments) and returns an output. To call a function,
you need to reference the function name followed by a set of
parenthesis.
"""

#Defining a function

def getsum(num1, num2):
    return num1 + num2
sum = getsum(12,25) #function call
print(sum) #37

#If a function does not explicitly return a value
# then the default return value is None:

def greet():
    print('hello')
hello = greet() # hello
print(hello) # None

def hi(greeting): 
        #greeting is called a parameter. (The Blueprint)
        # Think of it as a temporary placeholder
        # variable that only exists inside this function.
    return greeting 
hi_greeting = hi('hi') 
                    #The string 'hi' is the actual argument.(The Value)
                    #When you call hi('hi'), Python instantly assigns that argument to the parameter (greeting = 'hi').
print(hi_greeting)
#The function returns 'hi', and your variable hi_greeting successfully catches it so you can print it later.

#You can also supply default values to parameters like this:
def get_sum(num_1, num_2=2): #I declared the second parameter as 2 already
    return num_1 + num_2
result = get_sum(3) 
print(result) # 5
#default parameters must always come last in the function definition.

"""
If you call the function without the correct number of 
arguments, you will get a TypeError:

def calculate_sum(a, b):
    print(a + b)
calculate_sum()

TypeError: calculate_sum() missing 2 required positional
arguments: 'a' and 'b'
"""

print('-------------------------------')

#Common Built-in Functions

#input() Function: This is used to prompt the user for some input:
#input_name = input('What is your name?') # User Types Jay and presses Enter
#print('Hello', input_name) # Hello Jay

#int() Function: This is used to convert a number, boolean, or a numeric string into an integer:
print(int(3.14)) # from float convert into int = 3
print(int('12')) # from string convert into int = 12
print(int(True)) # from boolean convert into int = 1
print(int(False)) # from boolean convert into int = 2

#Scope in Python

#Local Scope
#when a variable declared inside a function or class can only be accessed
#within that function or class
def local_scope():
    local_num = 10
    print(local_num)

#Enclosing Scope
#when a function that's nested inside another function can access the variables
#of the function it's nested within.
def outer_scope():
    outer_msg = 'I\'m on the outer scope'
    def inner_scope():
        print(outer_msg)
    inner_scope # Called the function inside the function named outer scope
print(outer_scope()) # I'm on the outer scope
    
#Global Scope
#refers to variables that are declared outside any functions or classes which
#can be accessed from anywhere in the program.
tax = 0.25
def get_total(subtotal): #subtotal is parameter
    total = subtotal + (subtotal * tax)
    return total
print (get_total(100)) #125.0 , 100 is the argument for subtotal parameter

#Built in Scope
#Reserved names in Python for predefined functions, modules, keywords, and objects.
print(str(45)) # '45' str() makes the value a string
print(type(3.14)) # <class 'float'> type() shows what type of data is in the value
print(isinstance(3, str)) # False isinstance() checks the the first argument type using the second argument

#Comparison Operators

#Equal (==): Checks if two values are equal:
print(12 == 25) # False

#Not equal (!=): Checks if two values are not equal:
print(12 != 25) # True

#Strictly greater than (>): Checks if one value is greater than another:
print(12 > 25) # False

#Strictly less than (<): Checks if one value is less than another:
print(12 < 25) # True

#Greater than or equal (>=): Checks if one value is greater than or equal to another:
print(12 >= 25) # False

#Less than or equal (<=): Checks if one value is less than or equal to another:
print(12 <= 25) # True

print('-------------------------------')

#Working with if, elif and else statements

#if statements: These are conditions used to determine if something is true or not.
#if the condition evaluates to True, then that block of code will run.
if age >= 18:
    print('You are an adult') # You are an adult

#elif clause: These are conditions that come after an if statement. An elif clause
#runs only if all previous conditions evaluate to False and its own condition 
#evaluates to True.
elif_age = 22
if elif_age >= 18:
    print('You are an adult') # You are an adult
elif elif_age >= 13:
    print('You are a teenager') # You are a teenager

#else clause: This will run if no other conditions evaluate to True.
else_age = 22
if else_age >= 18:
    print('You are an adult') # You are an adult
elif else_age >= 13:
    print('You are a teenager') # You are a teenager
else:
    print('You are a child') # You are a child

#You can also use nested if statements like this:
is_citizen = True
citizen_age = 22

if is_citizen:
    if citizen_age >= 18:
        print('You are eligible to vote') # You are eligibe to vote
else:
    print('You are not eligible to vote')

"""
Truthy and Falsy Values
Every value has an inherent boolean value, or a built-in sense of whether
it should be treated as True or False in a logical context. Many values are
considered truthy, that is, they evaluate to True in a logical context. Others
are falsy, meaning they evaluate to False. Here are some examples of falsy values:

None
False
Integer 0
Float 0.0
Empty strings ''

Other values like non-zero numbers, and non-empty strings are truthy.
"""

print('-------------------------')

"""
Working with the bool() Function
If you want to check whether a value is truthy or falsy,
you can use the built-in bool() function. It explicitly
converts a value to its boolean equivalent and returns True
for truthy values and False for falsy values. Here are a few
examples:
"""

print(bool(False)) # False
print(bool(0))  # False
print(bool('')) # False
print(bool(True)) # True
print(bool(1)) # True
print(bool('Hello')) # True

"""
Boolean Operators and Short-circuiting
Definition: These are special operators that allow you to
combine multiple expressions to create more complex
decision-making logic in your code. There are three Boolean
operators in Python: and, or, and not.

and Operator: This operator takes two operands and returns
the first operand if it is falsy, otherwise, it returns the
second operand. Both operands must be truthy for an
expression to result in a truthy
"""
and_itstrue = True
and_itstrue_value = 25
print(and_itstrue and and_itstrue_value) #25

#You can also use the and operator in conditionals like this:

if and_itstrue and age >= 18:
    print('You are eligible to vote') # You are eligible to vote
else:
    print('You are not eligible to vote')

"""
or Operator: This operator returns the first operand if it
is truthy, otherwise, it returns the second operand. An or
expression results in a truthy value if at least one operand
is truthy. Here is an example:
"""
or_itsfalse = False
print(and_itstrue_value or or_itsfalse) # 25

#Just like with the and operator, you can use the or
#operator in conditionals like this:\

or_age = 19
or_isstudent = True

if or_age < 18 or or_isstudent:
    print('You are eligible for a student discount')
        # You are eligible for a student discount
else:
    print('You are not eligible for a student discount')

"""
Short-circuiting: The and and or operators are known as a
short-circuit operators. Short-circuiting means Python checks
values from left to right and stops as soon as it determines
the final result.


not Operator: This operator takes a single operand and inverts
its boolean value. It converts truthy values to False and
falsy values to True. Unlike the previous operators we looked
at, not always returns True or False. Here are some examples:
"""

print(not '') # True, because empty string is falsy
print(not 'Hello') # False, because non-empty string is truthy
print(not 0) # True, because 0 is falsy
print(not 1) # False, because 1 is truthy
print(not False) # True, because False is falsy
print(not True) # False, because True is truthy

#Here is an example of the not operator in a conditional:

is_admin = False

if not is_admin:
    print('Access denied for non-administrators.') # Access denied for non-administrators.
else:
    print('Welcome, Administrator!')

print('--------------------------------------------------')

"""
The list data type is an ordered sequence of elements that
can be comprised of strings, numbers, or even other lists.
Lists are mutable and use zero-based indexing, meaning that
the first element of the list is at index zero.
"""
#Here is the basic syntax for a list:
cities = ['Caloocan' , 'Quezon City', 'Manila']

"""To access an element from the cities list, you can
reference its index number in the sequence. Here is an
example of accessing the first element of the cities list:"""
cities[0] # 'Caloocan'

"""Negative indexing is used to access elements starting
from the end of the list instead of the beginning at index 0.
To access the last element of any list, you can use -1 like
this:"""
cities[-1] # 'Manila

#Another way to create a list is to use the list() constructor.
#The list() constructor is used to convert an iterable into a
#list like this:
developer = 'Christian'
list(developer) # ['C', 'h', 'r', 'i', 's', 't', 'i', 'a', 'n']

#To get the total number of elements in a list, you can use
#the len() function like this:
numbers = [1,2,3,4,5]
len(numbers) # 5

#If you wanted to update a value at a particular index, you
#can do something like this:
programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[0] = 'JavaScript'
print(programming_languages) # ['JavaScript', 'Java', 'C++', 'Rust']

"""
Since lists are mutable, you can update any element in the
list as long as you pass in a valid index number. If you pass
in an index (either positive or negative) that is out of
bounds for the list, then you will receive an IndexError:
"""

programming_languages = ['Python', 'Java', 'C++', 'Rust']
programming_languages[10] = 'JavaScript'

programming_languages = ['Python', 'Java', 'C++', 'Rust']
#programming_languages[10] = 'JavaScript'

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
IndexError: list assignment index out of range
"""

#If you want to remove an element from a list you can use
#the del keyword like this:

developer = ['Jay Sese', 22, 'Python Developer']
del developer[1] #index 1 is 22
print(developer) # ['Jay Sese' , 'Python Developer']

#Sometimes it is helpful to check if an element is inside
#the list. To do that, you can use the in keyword like this:

programming_languages = ['Python', 'Java', 'C++', 'Rust']
'Rust' in programming_languages # True
'JavaScript' in programming_languages # False

#Sometimes it is common to have lists nested inside of other
#lists like this:
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]

"""
In this example, we have one nested list containing three
popular programming languages. To access the nested list,
you will need to access it using index 2 since lists are 
zero based indexed:
"""
developer = ['Alice', 25, ['Python', 'Rust', 'C++']]
    #The nested list (the list inside the list) is index 2
developer[2] # ['Python', 'Rust', 'C++']

#Then to access the second language from that nested list,
#you will need to access it using index 1 like this:
developer[2][1] #Rust is index 1 on the nested list
    #Access the nested list then, index the value

"""
Another common technique used with lists is unpacking values.

Unpacking values from a list is a technique used to assign
values from a list to new variables. Here is an example of
unpacking a developer list into new variables called name,
age and job.
"""

developer = ['Alice', 34, 'Rust Developer']
name, age, job = developer

print(name) # 'Alice'
print(age) # 34
print(job) # 'Rust Developer'

#Putting lists values into a variable
#Here, name has the value 'Alice', age has the value 34,
#and job has the value 'Rust Developer'.

#If you need to collect any remaining elements from a list,
#you can use the asterisk (*) operator like this:

developer = ['Alice', 34, 'Rust Developer']
name, *rest = developer
#You assigned Alice into variable name
#Then you assigned THE REST OF THE VALUE IN THE DEVELOPER LIST into rest
print(name) # 'Alice'
print(rest) # [34, 'Rust Developer']

"""
In this example, name will still have the value 'Alice',
and rest is a list of two items: the number 34 and the
string 'Rust Developer'.

If the numbers of variables on the left side of the
assignment operator doesn't match the total numbers of items
in the list, then you will receive a ValueError:
"""
developer = ['Alice', 34, 'Rust Developer']
#name, age, job, city = developer
#theres not enough value in the list
#no value from the list to put as a city variable

"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: not enough values to unpack (expected 4, got 3)
"""

#The last concept we will look at is the slice operator (:).
# Similar to strings, you can access portions of a list by
# using the slice operator like this:

desserts = ['Cake', 'Cookies', 'Ice Cream', 'Pie', 'Brownies']
desserts[1:4] # ['Cookies', 'Ice Cream', 'Pie']
# You slice the lists from index 1 cookies to index 4 brownies
# but index 4 is not included so its just until index 3 which is pie

"""
In this example, the start index is 1 since that points to the
 second item in the list. Then we use the slice operator
 followed by an end index of 4, which includes everything up
 to (but not including), the item at that index.

Another thing you can do with the slice operator : is specify
a step interval which determines how much to increment
between the indices. Let's say you had a list of numbers like
this:
"""
numbers = [1, 2, 3, 4, 5, 6]

#If you wanted to extract a list of just even numbers, you
# can use the slicing operator like this:

numbers = [1, 2, 3, 4, 5, 6]
numbers[1::2] # [2, 4, 6]

#1 0  1
#2 1  2 select
#3 2  1
#4 3  2 select
#5 4  1 
#6 5  2 select
#stepping every 2 values start:stop:step

#It's like stepping on slicing strings.

"""
The first even number is at index 1, so that will be the
start index. Since we want to go through the end of the list,
then we omit the end index. Lastly, we specify 2 for the
optional step interval so it will only increment by 2 instead
of the default 1.

Lists are a useful and flexible data structure that you will
use a lot in your Python programs. In the next lesson, you
will learn about common methods that you can use with lists.
"""
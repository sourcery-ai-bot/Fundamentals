# Introduction to Python

There are several ways to work with python. You can create a file, for example `test.py` and then run it with the `python` command, i.e. `python test.py`.

Another way to use python is in the interactive interpreter. To access this, open up a terminal and type in python.

```
python

a = 1
b = 2
a + b

exit()
```

## Terminal Commands

`ls` - lists the files in the current directory.

`pwd` - print working directory

`cd` - change directory

## Exercise 01

Write a program that prompts a user for their name, and then greets them.

E.g. 

Question 1: What is your name?

Output: "Hello Fred! It's nice to meet you."

```python
# prompt a user to give their name, and assign it
# to the variable name.
first_name = input("What is your given name?\n")
last_name = input("What is your family name?\n")


# Interpolate the "name" variable into the greeting string
greeting = "Hello {family_name} {given_name}. It's nice to meet you.".format(given_name=first_name, family_name=last_name)
# greeting = "Hello {} {}. It's nice to meet you.".format(first_name, last_name)

# Print the greeting.
print(greeting)
```

## Working with Strings

Have a look at the [python docs](https://docs.python.org/2.5/lib/string-methods.html) for String Methods.

```
s = 'kiwi'
"My favorite fruit is {}".format(fruit)

me = "drew"
friend = "charles"
"{me} doesn't like {favorite_fruit}, but {friend} does.".format(me=me, favorite_fruit=fruit, friend=friend)
```

## Exercise 02

2a. Find a method in the docs to swap the case of letters in a string.

```
"HELLo" --> "hellO"
```
```python
"HELLo".swapcase()
```
2b. Replace a substring with another string.https://github.com/compsciacademy/Fundamentals

```
"Are you hungry?" --> "Are you thirsty?"
```
```python
"Are you hungry?".replace("hungry", "thirsty")
```

```
"Are you hungry?" --> "Am I hungry?"
```
```python
"Are you hungry?".replace("Are you", "Am I")
```

2c. Remove only the leading whitespace from a string, preserving the trailing whitespace.

```
"                How are you?             " --> "How are you?             "
```

```python
"                How are you?             ".lstrip()
```

## Math Operations

```python
5 * 5 # five times five
2 + 2 + 1
10 / 2 # what do you expect this to return?
10 // 2 # what do you expect this to return?
isinstance(10 / 2, int)
isinstance(10 / 2, float)
2 ** 10
10 % 3
```

## Exercise 03

1. Write code that asks a user for two inputs that are numbers, and returns the product of those numbers.

```python
first_number = input("Give me a number: ")

second_number = input("Give me another number: ")

print(int(first_number) * int(second_number))
```

# Comparison Operators

```
True
False
10 > 
5 < 2
True and True
True and (10 > 5)
True or False
10 >= 10 or False
5 == (2 + 3)
my_password = "secret"
my_saved_password = "super_secret"
my_password == my_saved_password

```

# Conditionals

Let's try using `if .. elif .. else`

```python
a = 5
if a > 15:
    print("Big number!")
elif a > 10:
    print("Medium number!")
else:
    print("Small number!")

```

## Exercise 04

Write code that asks users for the year of their car and then prints: future, new, old or very old, depending on the year.




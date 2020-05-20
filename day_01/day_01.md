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
2b. Replace a substring with another string.

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
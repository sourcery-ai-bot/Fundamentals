# Fundamentals Day 04  

Today, we are going to review some of the concepts that we have introduced, and expand upon them.

## Data Types

An `int` is a whole number. 1, 164, 6999 are integers. The range supported by the int type is -2147483648 through 2147483647.

A `float` or a floating point number has a decimal. 1.1, 3.14, 68.126123123 are floats.

A `str` or string is something wrapped in quotes. In python we can use single quotes or double quotes interchangably, as long as we are consistent. 

Examples:

```python
# assign int values to two variables, a and b:
a = 1
b = 2

# some operations we can perform on integers are:
a + b
b * 3
c = b / a

# we can interpolate the value of variables in strings.
# Let's do it!
favorite_candy = "Skittles"

"Allan's favorite candy is {}.".format(favorite_candy)

# we can also concatenate strings using the
# concatenation operator.

"Allan's favorite candy is" + " " + favorite_candy + "."
```

## Functions

Functions are great for allowing us to do something repeatedly. We can define a thing, or things that need to be done, and group them together using functions.

Examples:

```python
def prepare_greeting(name):
    return "Hello {}! It's nice to see you!".format(name)

def get_name():
    first_name = input("What is your first name?")
    last_name = input("What is your last name?")
    return first_name + " " + last_name

def greet():
    name = get_name()
    greeting = prepare_greeting(name)
    print(greeting)

greet()

# variadic parameters
def list_names(*names):
    for name in names:
        print("Hello " + name +"!")
```

## Data Structures

A list `[]` can be filled with items of any type, and we can iterate over the list, or do many other things with it. There are several built in methods that can be called on lists. We can also create our own functions for working with them.

Let's create a shopping list. I should be able to add items to the list, and then remove them from the list after I buy them (or add them to a cart).

```

```


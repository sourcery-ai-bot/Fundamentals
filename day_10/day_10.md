# Fundamentals Day 10

Let's build on the Cat competition application we worked on last time, and create a user interface. Also, let's have a way for a user to create a character (a cat), and compete against other users.

## Exercise 01

First, start out with a command line interface, like we're familiar with. Then, we will have a look at using a web browser based interface.  
  
```
CompetitionCats!

n  make a new cat
u  use an existing cat
q  quit

What would you like to do?
```

## Exercise 02

Create a method on the class `Cat` called `save()` so that when `Cat("CatName").save()` is called, it will write the cat information to a file. Maybe something like `cats.db` or `cats_db.txt`

Here's a starter `Cat` class:

```python
class Cat:
    def __init__(self, name):
        self.name = name

    def save(self):
        pass

```

## Exercise 03

Now that we are able to read and write cat data to a data store (a file, in this case), let's give cats more attributes, so that they are useful for competitions. Let's also return a cat object with a Class method on the `Cat` class `find_cat_by_name("Blinky")`.

a.) Give cats more attributes: `energy`, `pride`, `size`. Energy and pride should be of type `int` and size should be of type `str`, and one of the following: "small", "medium", "large"

**HINT**: use the `random` library `import random` to generate random integers, e.g. `random.randint(10, 25)` will return an integer in the range between 10 and 25.

User `random.choice()` to select from a list of strings, e.g. `random.choice(['red', 'green', 'blue'])` will return one of 'red', 'green', 'blue'.

b.) Create a class method on the `Cat` class called `find_by_name()` that takes an argument of type `str`, looks for the cat in the cats data store, and returns a cat object.

## Exercise 04 (Homework)

Add some additional functionality to the CompetitionCats application. Users should be able to select a cat, and engage in a competition with another cat.

a.) Think through what the choices a user should have will be.  
b.) Think through what competitions should be implemented, and how they will work.  
c.) After you have given it some thought, try implementing it.  

## Brief introduction to HTML

HTML is a language we use to organize information on a web page. It's pretty straight forward, and fun!

Here's a legend of how HTML works:
```html
<element attribute='value'></element>
```

Here's a real example of an HTML web page:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>My Super Awesome Website</title>
    </head>
    <body>
        <h1>Welcome to My Website!</h1>
        <p>This is a paragraph about my website</p>
    </body>
</html>
```

**BONUS**: The [Google HTML/CSS Styleguide](https://google.github.io/styleguide/htmlcssguide.html) is a great resource!





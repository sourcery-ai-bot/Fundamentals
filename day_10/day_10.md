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

b.) Create a class method on the `Cat` class called `find_by_name()` that takes an argument of type `str`, looks for the cat in the cats data store, and returns a cat object.

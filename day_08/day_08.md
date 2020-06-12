# Fundamentals Day 08

Let's review day 07. We had an assignment to write an application for interacting with authors and book data.

This was originally discussed in [module 02](https://github.com/compsciacademy/Fundamentals/blob/master/day_02/day_02.md#dictionaries):

## Dictionaries

In python there is a data type that maps `key:value` pairs, that we call a dictionary.

```python
books = {"Author": ["list", "of", "titles"]}

books = {
    "Pinker": ["The Language Instinct", "How the Mind Works", "Words and Rules"], 
    "Dawkins": ["The Selfish Gene", "The Extended Phenotype", "The Blind Watchmaker"]
}
```

## Homework Assignment for Module 02

Write a program that asks a user what the user wants to do. The choices are:
view authors, view books by author, add authors, add books to authors.

In Module 07, [Exercise 03](https://github.com/compsciacademy/Fundamentals/blob/master/day_07/day_07.md#exercise-03) we discussed what the data might look like, and came up with a couple of options:

  - A single dictionary whose keys are strings of author names, and whose values are lists of strings of book titles
  - A list of dictionaries whose keys are `author` (which has string values) and `books` (which has lists of strings as values)

Then, we discussed what the data might look like in a file we are storing it in. We decided we can have an author's name, followed by a comma, and then a list of comma book titles for that author.

We left off by setting up the tests for Exercise 03 a:

Write function that will read data from the data storage (in this case a file). But, before you do, write a test.
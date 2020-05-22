# Fundamentals Day 02

```python
count = 0
while count < 10:
    # do something
    print("I am doing something")
    #count = count + 1
    count += 1

count = 0
while True:
    print("Hello. Truth is true!")
    count += 1
    if count > 2:
        break

```

## Exercise 01

Print numbers 50 to 1 using a while loop.

```python
count = 50
while count >= 1:
    print(count)
    count -= 1
```

## Exercise 02

Print the first 30 _odd_ numbers using a while loop.

```python
count = 1
number = 1
while count <= 30:
    if number%2 == 1:
        print(number)
        count += 1
    number += 1

```

There is also a `for` loop. For is quite useful for working with `lists`. Let's take a look at both!

Before we talk about `for`, let's look at lists.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers[0]

words = ['apple', 'pear', 'spaghetti', 'elephant']

words[3] = 'bear'
words.append('tiger')
```

```python
students = ['Emily', 'Jason', 'Jackson', 'Allan', 'Alex', 'Brandon']

for item in students:
    print(item)

index = 0
while index < len(students):
    print(students[index])
    index += 1

student[0]
len(students) # 6

last_student = students[len(students)-1]
```
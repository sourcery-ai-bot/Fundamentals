# Fundamentals Day 12  

Using flask,

```python
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def lol():
    return 'Hello, and LoL!'

app.run()

```

## Exercise 01

Have a look at the following flask application:

Web Server:
`app.py`
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        return 'Hello!'

app.run()
```

Web Templates (View):
`templates/index.html`
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Home</title>
    </head>
    <body>
        <h1>Home</h1>
        <p>Welcome to my home page!</p>

        <p>What is your name?</p>
        <form method='POST'>
            <input name='name'><input type='submit' value='Go!'>
        </form>
    </body>
</html>

```
a.) In the `index()` method, use some code to return a greeting to the name entered by the user, e.g. "Hello, Sal!"

b.) Instead of returning a string, write a template that greets the user by name, and is rendered if a post request has been sent to `index()`

## Exercise 02

a.) Let's implement a system for gathering names and email addresses of users. If both name and email are not submitted, it should not save a new user, but rather prompt the user to enter again.

b.) We should be able to save user information. While duplicate names are OK, we want to ensure there are no duplicate email entries.

c.) Let's also create a view that lists all users, sorted alphabetically by name.

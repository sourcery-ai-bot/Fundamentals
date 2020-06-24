# Fundamentals Day 11  
  
HTML is a language we use to organize information on a web page. It's pretty straight forward, and fun!

Here's a legend of how HTML works:

<element attribute='value'></element>
Here's a real example of an HTML web page:

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
BONUS: The [Google HTML/CSS Styleguide](https://google.github.io/styleguide/htmlcssguide.html) is a great resource!

Here's an example of a form:
```html
<html>
    <head>
        <title>My Super Awesome Website</title>
    </head>
    <body>
        <form method='POST'>
            <input name='email'>
            <input name='password'>
            <input type='submit'>
        </form>
    </body>
</html>

```
Looking at the CompetitionCats commandline UI, the initial prompt is:
```
CompetitionCats!

Menu
n  make a new cat
u  use an existing cat    
q  quit

What would you like to do?
```

Something similar in an HTML GUI would be:
```html
<!DOCTYPE html>
<html>
    <head>
        <title>CompetitionCats: Menu</title>
    </head>
    <body>
        <h1>Competition Cats</h1>
        <h2>Menu</h2>
        <ul>
            <li>n &nbsp; make a new cat</li>
            <li>u &nbsp; use an existing cat</li>
        </ul>
        <form method='POST'>
            selection: <input name='user_choice'><input type='submit'>
        </form>
    </body>
</html>
```

## Exercise 01

Think through the rest of the user interface, and choose 1 view to convert to HTML.

## Web Development with Flask  
  
If you haven't already, now is a good time to install [Flask](https://flask.palletsprojects.com/en/1.1.x/).

```
pip install flask

# or maybe

pip3 install flask
```

Flask gives use some tools we can use to handle incoming requests, and serve web pages.

## Exercise 02

With the basics of `GET` and `POST` that we have just learned in our example web application, let's add a GUI (web ui) to our CompetitionCats App, making it a Web App.

Example Web Server
```py
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/name', methods=['GET', 'POST'])
def greet():
    if request.method == 'GET':
        return render_template('name_form.html')
    elif request.method == 'POST':
        return "Hello there, {}!".format(request.form['name'])
    else:
        return "Unable to handle request type: {}".format(request.method)


app.run()
```

Example Web Page (server by our Example Web Server)

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Name</title>
    </head>
    <body>
        <form method='POST'>
            What is your name? <input name='name'><input type='submit'>
        </form>
    </body>
</html>
```

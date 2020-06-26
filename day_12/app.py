from flask import Flask, render_template, request
from user import User

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        if len(name) < 2 or len(email) < 5:
            return render_template('index.html')
        else:
            user = User(name, email)
            if user.save():
                return render_template('greet.html', name = user.name)
            return render_template('index.html')

@app.route('/users', methods=['GET'])
def users():
    return render_template('users.html', users = User.all())

app.run(debug=True)

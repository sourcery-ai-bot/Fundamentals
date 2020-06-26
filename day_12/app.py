from flask import Flask, render_template, request

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
            return render_template('greet.html', name = name)
app.run()

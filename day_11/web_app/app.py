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

@app.route('/names', methods=['GET'])
def names():
    all_names=['Emily', 'Jackson', 'Jason', 'Allan', 'Brandon', 'Drew']
    return render_template('names.html', names=all_names)


app.run()
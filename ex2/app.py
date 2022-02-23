from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc')
def calc():
    number = request.args.get('inpu')
    if not number.isnumeric():
        return render_template('calc.html', evodd = "not a number!" )
    
    if int(number)%2 == 1:
        result = number + " is odd"
        return render_template('calc.html', evodd = result )
    else:
        result = number + " is even"
        return render_template('calc.html', evodd = result )
    
from flask import Flask, render_template, request

app=Flask(__name__)

Dict = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registered', methods= ['GET', 'POST']) 
def registered():
    name = request.form.get('fullname')
    org = request.form.get('org')
    Dict[name] = org
    return render_template('register.html', result = Dict)

from flask import Flask,render_template,request, redirect,session
from db import Database
import api

app = Flask(__name__)  # through provide the __name__ the flask know where the flask application are located   .

dbo = Database()

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registration', methods = ['post'])
def perform_registration():
    name = request.form.get('user_ka_name')
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.insert(name,email,password)

    if response:
        return render_template('login.html',message = 'Registration Successful. Kindly login to proceed')
    else:
        return render_template('register.html', message = 'Email already exists')


@app.route('/perform_login', methods = ['post'])
def perform_login():
    email = request.form.get('user_ka_email')
    password = request.form.get('user_ka_password')

    response = dbo.search(email,password)
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html', message = 'incorrect email/password')


@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')
@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')


@app.route('/perform_ner', methods = ['post'])
def perform_ner():
    if session:
        text = request.form.get('ner_text')
        response = api.ner(text)
        print(response)

        result = ''
        for word, entity_group in response:
            result = result + word + " " + entity_group + "\n"

        return render_template('ner.html', result = result)
    else:
        return redirect('/')




app.run(debug = True)

from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

from requests_cache.policy import expiration

app = Flask(__name__)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    token = db.Column(db.String(255))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        print('I want to register...!')
        return render_template('register.html')
    else:
        user = User(request.form['username'], request.form['email'], request.form['password'])
        db.session.add(user)
        db.session.commit()
        flash("Регистрация прошла успешно!")
        return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print ('I want to login!')
        return render_template('login.html')
    else:
        user = User.query.filter_by(username=request.form['username']).first()
        if user.password == request.form['password']:
            token = user.token
            expiration = datetime.now() + timedelta(minutes=15)
            session['token'] = token
            return redirect(url_for('register'))
        else:
            fash("Неправельно введены данные!")
            return render_template('login.html')

@app.before_request
def chech_auth():
    token = session.get('token')
    if not token or datetime.now() > expiration:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('token')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
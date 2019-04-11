from flask import Flask, render_template, flash, redirect, url_for, request, session

from wtforms import Form, TextField, PasswordField, validators
from passlib.hash import sha256_crypt #To hash Passwords
from MySQLdb import escape_string as thwart #To not interfere with SQL commands

from dbconnect import connection
import gc

app = Flask(__name__)

if __name__== '__main__':
    app.run(debug=True)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = None
    if request.method == 'POST':
        if (request.form.get("username",False) != 'admin' or
request.form.get("password", False) != 'admin'):
            error = 'Invalid Credentials. Please try again'
        else:
            return redirect(url_for('home'))
    return render_template('signin.html', error=error)

class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min = 4, max = 20)])
    email = TextField('Email Address', [validators.Length(min = 6, max = 50)])
    password = PasswordField('Password', [validators.Required(),
                                            validators.EqualTo('Confirm', message = "Passwords must match")])
    confirm = PasswordField('Repeat Password')


@app.route('/registration', methods = ["GET", "POST"])
def register_page():
        form = RegistrationForm(request.form)

        if request.method == "POST" and form.validate():
            username = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            c, conn = connection()

            x = c.execute("SELECT * FROM users WHERE usernames = (%s)",
                            (twart(username)))

            if x:
                flash("That username is already taken, please choose another")
                return render_template('registration.html', form = form)

            else:
                c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)",
                            (thwart(username), thwart(password), thwart (email), thwart("/about")))
                conn.commit()

                flash("Thanks for registering!")
                c.close()
                conn.close()

                gc.collect() #To enforce Python to clean it's 'garbage'

                session ['logged_in'] = True
                session ['username'] = username

                return redirect(url_for('/'))

            return render_template("registration.html", form=form)

from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

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

@app.route('/about')
def about():
    return render_template('about.html')

if __name__== '__main__':
    app.run(debug=True)


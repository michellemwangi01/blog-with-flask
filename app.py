from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

# START THIS APP:
# OPTION 1: creating an environment variable for it on the terminal. Make sure no spaces between the = sign
# 1. ` export FLASK_APP=app.py ` or ` FLASK-DEBUG=1 `
# 2. flask run

# OPTION 2: Running the file directly
# 1. Add the if main checker in debug mode as below and run the file directly.
# 2. on the terminal run, `python3 app.py`

# PACKAGES EXPLAINED
# url-for, helps to find the location of files automatically instead of manually typing the path
# install wtforms in order to manage forms in flask `pip install flask-wtf`

# Instantiates a new Flask application stored in app variable
app = Flask(__name__)

# GENERATING SECRET FOR THE APP
#  when collecing, validating user input , its important to protect against cross-site scripting and protect cookies etc. We do this my generating a random characters.
# This can be obtained by
# 1. enter the python interpretor by running `python3` in the terminal
# 2. run `import secrets`
# 3. run `secrets.token_hex(16)` 16 being the number of bytes
# 4. copy the value returned and pass it below
app.config['SECRET_KEY'] = '2de465031cfc53df83c21f2e374b84a0'
blogposts = [
    {
        'author': 'corey schaffer',
        'title': 'Flask Tutorials',
        'content': " 'Youtube Tutorials' ",
        'date_posted': 'September 12, 2023'
    },
    {
        'author': 'michelle mwangi',
        'title': 'moringa journey',
        'content': " 'Phase 1 journey' ",
        'date_posted': 'July 12, 2023'
    },
    {
        'author': 'ashfa wade',
        'title': 'The transition',
        'content': " 'From a Boy to a Man' ",
        'date_posted': 'February 02, 2023'
    },

]


@app.route("/")  # the route that allows navigateion to the different pages of the website. This defines the root or
# the home page of the app. Routes for the specific pages are handled using the route decorator.
@app.route("/home")  # can have multiple routes defined for a single path.
def home():
    return render_template('home.html', posts=blogposts, title='Home Page')


@app.route("/about")  # the route that allows navigateion to the different pages of the website. This defines the
# root or the home page of the app. Routes for the specific pages are handled using the route decorator.
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        flash(f'Account created for {registration_form.username.data}!', category='success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=registration_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    return render_template('login.html', title='Login', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)

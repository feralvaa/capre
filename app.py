from flask import Flask, render_template
# from forms import RegistrationForm, LoginForm

app = Flask(__name__)
# secret key
app.config['SECRET_KEY'] =  '424587ba6b2905c5075ee379cabf60f5767936995e78a754b9786f517c994d76'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
     return render_template('about.html')


# @app.route("/register")
# def register():
#      form = RegistrationForm()
#      return redender_template ('register.html', title= 'Register', form=form)

# @app.route("/login")
# def login():
#      form = LoginForm()
#      return redender_template ('login.html', title= 'Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)

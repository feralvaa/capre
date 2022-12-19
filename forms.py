# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField, BooleanField
# from wtforms.validators import Datarequired, Lenght, Email, EqualTo

# class RegistrationForm(FlaskForm):
#     #check validation / Data required -> 
#     username = StringField ('Username',
#                              validators= [DataRequired(), Length(min=2, max=20 )])

#     email = StringField ('Email',
#                             validators= [DataRequired(),Email()])

#     #Passwords
#     password = PasswordField('Password', validators = [DataRequired()])
#     confirm_password = PasswordField ('Confirm Password', 
#                                         validators=[DataRequired(),EqualTo('password')])
#     submit= SubmitField('Sign Up')

# class LoginForm(FlaskForm):
   
#     email = StringField ('Email',
#                             validators= [DataRequired(),Email()])

#     password = PasswordField('Password', validators = [DataRequired()])
#     remeber = BooleanField('Remember Me')
#     submit= SubmitField('Login')



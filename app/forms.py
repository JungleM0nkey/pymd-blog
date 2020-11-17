from flask_wtf import FlaskForm,  RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In', id='submit-button')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=16)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=64)])
    password_confirm = PasswordField('Confirm Password', validators=[DataRequired(), Length(max=64)])
    email = StringField('Email', validators=[DataRequired(), Email("This field requires a valid email address")])
    invite_code = StringField('Invite Code', validators=[DataRequired()])
    submit = SubmitField('Register', id='submit-button')
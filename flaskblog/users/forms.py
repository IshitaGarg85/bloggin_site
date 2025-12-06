from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField, FileField
from wtforms.validators import DataRequired, EqualTo, Length, Email
from flaskblog.models import User
from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileAllowed

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max = 20)] )
    email = StringField('email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('confirm_Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('signUp')
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first() 
        if user:
            raise ValidationError('This Username already exists!','danger')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first() 
        if user:
            raise ValidationError('This email already exists!','danger')


class LoginForm(FlaskForm):
    email = StringField('email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('remember_me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max = 20)] )
    email = StringField('email', validators = [DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators = [FileAllowed(['jpg', 'png'])])
    submit = SubmitField('update info')
    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first() 
            if user:
                raise ValidationError('That username already exists!','danger')
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first() 
            if user: 
                raise ValidationError('That email already exists!','danger')



class RequestResetForm(FlaskForm):
    email = StringField('email', validators = [DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first() 
        if user is None:
            raise ValidationError('There is no account with that email. You must Register first!','danger')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('confirm_Password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

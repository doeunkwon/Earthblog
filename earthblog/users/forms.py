# users/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField,FileAllowed
from flask_login import current_user
from earthblog.models import User

class LoginForm(FlaskForm):
    email = StringField('Email ',validators=[DataRequired(),Email()])
    password = PasswordField('Password ',validators=[DataRequired()])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    email = StringField('Email ',validators=[DataRequired(),Email()])
    username = StringField('Username ',validators=[DataRequired()])
    password = PasswordField('Password ',validators=[DataRequired(),
                                EqualTo('pass_confirm',message='Passwords must match.')])
    pass_confirm = PasswordField('Confirm password ',validators=[DataRequired()])
    submit = SubmitField('Register')
    def validate_email(self,email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('The email has been registered already.')
    def validate_username(self,username):
        if User.query.filter_by(username=self.username.data).first():
            raise ValidationError('The username has been registered already.')

class UpdateUserForm(FlaskForm):
    email = StringField('Email ',validators=[DataRequired(),Email()])
    username = StringField('Username ',validators=[DataRequired()])
    picture = FileField('Profile picture',validators=[FileAllowed(['jpg',
                        'png','JPEG'])])
    submit = SubmitField('Update')
    def validate_email(self,field):
        if current_user.email == field.data:
            return
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('The email has been registered already.')
    def validate_username(self,field):
        if current_user.username == field.data:
            return
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('The username has been registered already.')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import InputRequired
from wtforms.fields.html5 import EmailField


class RegistrationForm(FlaskForm):
  name = StringField('Username', validators=[InputRequired(), validators.Length(11,100)])
  username = StringField('Username', validators=[InputRequired(), validators.Length(11,100)])
  email = EmailField('Email Address', validators=[DataRequired(), validators.Email()])
  biography = TextAreaField('Biography', validators=[DataRequired(), validators.Length(11,100)])
  location = StringField('Location', validators=[InputRequired()])
  password = PasswordField('New Password', validators=[Required(), validators.EqualTo('confirm', message='Passwords must match!')])
  confirm = PasswordField('Confirm Password')
  date_joined = datetime.now()
  photo = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg','png'], 'Images Only!')])

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, DataRequired
from flask_wtf.file import FileField, FileAllowed

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])




class UploadForm(FlaskForm):
    file = FileField('Image File', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])

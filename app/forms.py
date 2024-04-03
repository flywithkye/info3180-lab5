# Add any form classes for Flask-WTF here
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, SelectField
from wtforms.widgets import TextArea
from wtforms.validators import InputRequired

class MovieForm(FlaskForm):
    
    title = StringField('Title', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()], widget=TextArea())
    
    poster = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'jpeg', 'png'], 'PNG, JPG/JPEG Images only!')
    ])
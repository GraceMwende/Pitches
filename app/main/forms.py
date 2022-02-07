from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
  title = StringField('Title', validators=[InputRequired()])
  category =StringField('Category',  validators=[InputRequired()])
  description = StringField('Description', validators=[InputRequired()])
  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us abou you', validators=[InputRequired()])
  submit = SubmitField('Submit')
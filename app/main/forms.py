from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
  title = StringField('Title', validators=[InputRequired()])
  category =StringField('Category',  validators=[InputRequired()])
  description = TextAreaField('Description', validators=[InputRequired()])
  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you', validators=[InputRequired()])
  submit = SubmitField('Submit')
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
  title = StringField('Title', validators=[InputRequired()])
  category =SelectField('Category',choices=[('int','Interview'),('promotion','promotion'),('tech','technology'),('pick','pickuplines')],  validators=[InputRequired()])
  description = TextAreaField('Description', validators=[InputRequired()])
  submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
  bio = TextAreaField('Tell us about you', validators=[InputRequired()])
  submit = SubmitField('Submit')
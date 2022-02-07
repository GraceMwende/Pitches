from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm
from ..models import Pitch
from flask_login import login_required

# Pitch = pitch.Pitch

#views
@main.route('/')
def index():
  """View page that returns the index page and its data"""

  # Get promotion pitches
  category = "promotions"
  title = "Banking Finance"
  description = "I want the latest in...'re committed to your privacy. HubSpot uses the information you provide to us to contact you about our relevant content, products, and services. You may unsubscribe from these communications at any time"

  return render_template('index.html', category=category, title=title, description=description)

@main.route('/pitch/<pitch_id>')
def pitch(pitch_id):
  """view pitch page function that returns pitch details and its data"""

  return render_template('pitch.html', id=pitch_id)

# @main.route('/pitch/new/<int:id>', methods=["GET","POST"])
# def new_pitch(id):
#   form = PitchForm()
#   # pitch = ()

#   if form.validate_on_submit():
#     title = form.title.data
#     pitch = form.description.data
#     category = form.category.data
#     new_pitch.save_review()

#   return render_template('new_pitch.html', pitch_form=form)

@main.route('/pitch/new', methods=["GET","POST"])
@login_required
def new_pitch():
  form = PitchForm()
  # pitch = ()

  if form.validate_on_submit():
    title = form.title.data
    pitch = form.description.data
    category = form.category.data
    new_pitch.save_review()

  return render_template('new_pitch.html', pitch_form=form)

@main.route('user/<uname>')
def profile(uname):
  user = User.query.filter_by(username=uname).first()

  if user is None:
    abort(404)

  return render_template('profile/profile.html', user=user)
from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,UpdateProfile
from ..models import Pitch,User
from flask_login import login_required,current_user
from .. import db,photos

# Pitch = pitch.Pitch

#views
@main.route('/',methods=["GET","POST"])
def index():
  """View page that returns the index page and its data"""

  pitches = Pitch.query.all()
  interview = Pitch.query.filter_by(category='interview').all()
  promotion = Pitch.query.filter_by(category='promotion').all()
  tech = Pitch.query.filter_by(category='technology').all()
  pickup = Pitch.query.filter_by(category='pickuplines').all()

  return render_template('index.html',pitches=pitches, interview=interview, promotion=promotion, tech=tech,pickup=pickup)

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

@main.route('/pitch/new/<int:id>', methods=["GET","POST"])
@login_required
def new_pitch(id):
  form = PitchForm()
  user = User.query.filter_by(id=id).first()

  if form.validate_on_submit():
    title = form.title.data
    description = form.description.data
    category = form.category.data

    new_pitch = Pitch(title=title,description=description,pitch=current_user,category=category)

    new_pitch.save_pitches()
    return redirect(url_for('.profile', uname=user.username))
    

  return render_template('new_pitch.html', pitch_form=form)

@main.route('/user/<uname>')
def profile(uname):
  user = User.query.filter_by(username=uname).first()

  pitches = Pitch.get_pitches(user.id)

  if user is None:
    abort(404)

  return render_template('profile/profile.html', uname=user.username,user=user, pitches = pitches)

@main.route('/user/<uname>/update', methods=["GET","POST"])
@login_required
def update_profile(uname):
  user = User.query.filter_by(username=uname).first()
  if user is None:
    abort(404)

  form = UpdateProfile()

  if form.validate_on_submit():
    user.bio = form.bio.data

    db.session.add(user)
    db.session.commit()

    return redirect(url_for('.profile', uname=user.username))

  return render_template('profile/update.html', form=form)

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
  user = User.query.filter_by(username=uname).first()
  if 'photo' in request.files:
    filename=photos.save(request.files['photo'])
    path=f'photos/{filename}'
    user.profile_pic_path = path
    db.session.commit()
  
  return redirect(url_for('main.profile', uname=uname))
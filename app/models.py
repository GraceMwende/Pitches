from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class Pitch(db.Model):
  """Pitch class to define pitches"""
  __tablename__ = 'pitches'
  id = db.Column(db.Integer,primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  title = db.Column(db.String(255))
  description = db.Column(db.String(255))
  # comments = db.relationship('Comments', backref='comment', lazy='dynamic')

  def save_pitches(self):
    db.session.add(self)
    db.session.commit()
  
  @classmethod
  def get_pitches(cls,id):
    pitches = Pitch.query.filter_by(user_id =id).all()
    return pitches


# @classmethod
# def get_pitches(cls):
#   response = []
#   response.append()

# class Category(db.Model):

#   __tablename__ = 'categories'
#   id = db.Column(db.Integer, primary_key=True)
#   title = db.Column(db.String(255))
#   user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

# class Comments(db.Model):

#   __tablename__ = "comments"
#   id = db.Column(db.Integer,primary_key=True)
#   username = db.Column(db.String(255))
#   description = db.Column(db.String(255))
#   pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))

# def __repr__(self):
#   return f'Category {self.title}'

class User(UserMixin,db.Model):

  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255), unique=True, index=True)
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  # categories = db.relationship('Category', backref='role', lazy='dynamic')
  pitches = db.relationship('Pitch', backref='pitch', lazy='dynamic')
  pass_secure = db.Column(db.String(255))
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self,password):
    self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.pass_secure, password)

  def __repr__(self):
    return f'User {self.username}'


class Role(db.Model):

  __tablename__ = 'roles'
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.String(255))
  users = db.relationship('User', backref='role', lazy='dynamic')

def __repr__(self):
  return f'User {self.name}'


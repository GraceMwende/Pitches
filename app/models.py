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
  category = db.Column(db.String(255))
  title = db.Column(db.String(255))
  description = db.Column(db.String(255))
  comments = db.relationship('Comments', backref='comments', lazy='dynamic')
  likes = db.relationship('Likes', backref='likes', lazy='dynamic')
  dislikes = db.relationship('Dislikes',backref='dislikes',lazy='dynamic')

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

class Comments(db.Model):

  __tablename__ = "comments"
  id = db.Column(db.Integer,primary_key=True)
  # username = db.Column(db.String(255))
  description = db.Column(db.String(255))
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  

  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,id):
    comments = Comment.query.filter_by(pitch_id =id).all()
    return comments

  def __repr__(self):
    return f'comment {self.description}'

class Likes(db.Model):
  __tablename__ = 'likes'
  id = db.Column(db.Integer, primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def save_like(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_like(cls,id):
    likes = Likes.query.filter_by(pitch_id =id).all()
    return likes

  def __repr__(self):
    return f'comment {self.description}'

class Dislikes(db.Model):
  __tablename__ = 'dislikes'
  id = db.Column(db.Integer, primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,id):
    comments = Comment.query.filter_by(pitch_id =id).all()
    return comments

  def __repr__(self):
    return f'comment {self.description}'

class User(UserMixin,db.Model):

  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  email = db.Column(db.String(255), unique=True, index=True)
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  # categories = db.relationship('Category', backref='role', lazy='dynamic')
  pitches = db.relationship('Pitch', backref='pitch', lazy='dynamic')
  comments = db.relationship('Comments', backref='user', lazy='dynamic')
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


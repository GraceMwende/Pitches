from . import db
from werkzeug.security import generate_password_hash,check_password_hash

class Pitch:
  """Pitch class to define pitches"""

  all_pitches = []

  def __init__(self,id,category,title,description):
    self.id = id
    self.category = category
    self.title = title
    self.decription = description

  @classmethod
  def  get_pitches(cls):
    response = []
    response.append()

class User(db.Model):

  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(255))
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  pass_secure = db.Column(db.String(255))

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

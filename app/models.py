from . import db

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

  def __repr__(self):
    return f'User {self.username}'

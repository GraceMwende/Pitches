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

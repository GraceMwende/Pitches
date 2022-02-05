import unittest
from app.models import pitch
# Pitch = pitch.Pitch

class PitchTest(unittest.TestCase):
  """Test Class to test the behaviour of the Pitch class"""

  def setUp(self):
    """setup method that will run before every Test"""
    self.new_pitch = Pitch(5,"promotion","Banking success","This is where great minds meet and great things happen")

  def test_instance(self):
    """checks if object is an instance of the class"""
    self.assertTrue(isinstance(self.new_pitch,Pitch))
  
  def test_init(self):
    """check if the object is instantiated,correctly"""
    self.assertEqual(self.new_pitch.id, 5)
    self.assertEqual(self.new_pitch.category, "promotion")
    self.assertEqual(self.new_pitch.title, "Banking success")
    self.assertEqual(self.new_pitch.decription, "This is where great minds meet and great things happen")

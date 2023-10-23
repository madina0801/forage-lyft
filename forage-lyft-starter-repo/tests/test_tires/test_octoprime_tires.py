import unittest
from tires.octoprime_tires import OctorpimeTires

class TestOctoprimeTires(unittest.TestCase):
	def needs_service_true(self):
		tire_wear = [0.8, 0.8, 0.8, 0.7]
		tires = OctorpimeTires(tire_wear)
		self.assertTrue(tires.needs_service())

	def needs_service_false(self):
		tire_wear = [0.1, 0.2, 0.3, 0.2]
		tires = OctorpimeTires(tire_wear)
		self.assertFalse(tires.needs_service())
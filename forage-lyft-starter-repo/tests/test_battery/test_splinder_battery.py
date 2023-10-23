import unittest
from datetime import date

from battery.splinder_battery import SplinderBattery

class TestSplinderBattery(unittest.TestCase):
	def needs_service_true(self):
		current_date = date.fromisoformat("2020-05-15")
		last_service_date = date.fromisoformat("2018-01-20")
		battery = SplinderBattery(current_date, last_service_date)
		self.assertTrue(battery.needs_service())

	def needs_service_false(self):
		current_date = date.fromisoformat("2020-05-15")
		last_service_date = date.fromisoformat("2020-04-15")
		battery = SplinderBattery(current_date, last_service_date)
		self.assertFalse(battery.needs_service())
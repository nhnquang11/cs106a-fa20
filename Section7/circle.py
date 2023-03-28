import math

class Circle():
	def __init__(self, radius):
		"""
		Creates a Circle object and initialises the radius.
		"""
		self.radius = radius

	def get_area(self):
		"""
		Returns the area of this circle.
		"""
		return math.pi * (self.radius ** 2)

	def get_circumference(self):
		"""
		Returns the circumference of this circle.
		"""
		return 2 * math.pi * self.radius

from .street import Street
from .car import Car
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
	
class Intersection:

	def __init__(self, id, incoming: [Street]):
		super().__init__()
		self.id = id
		self.incoming = incoming

	def __repr__(self):
		return "{} {}".format(self.id, self.incoming)


	def reset_run(self):
		self.t = 0
		self.run_incoming = [*self.incoming]

	def next(self):
		if len(self.run_incoming) <= 0:
			return
		street = self.run_incoming[0]
		score = 0
		if street != None:

			score = street.next()

			self.t += 1
			if self.t > street.delay:
				self.run_incoming= self.run_incoming[1:] + self.run_incoming[:1]
				self.t = 0
		

		return score
		
	# def set_cars(self, cars: [Car]):
	# 	self.cars = [car for car in cars if car.road_map[0] == self]
	
	# def set_light(self, delay, color: Color):
	# 	self.light = (delay, color)
	# 	self.origin_delay = delay

	# def next(self) -> int:
	# 	"""next

	# 	Returns:
	# 		int: Number of cars finished
	# 	"""

	# 	if self.light[1] == Color.GREEN:




	# 	self.light[0] -= 1
	# 	if self.light[0] < 0:
	# 		self.light = (self.origin_delay, Color.RED if self.light[1] == Color.GREEN else Color.GREEN)


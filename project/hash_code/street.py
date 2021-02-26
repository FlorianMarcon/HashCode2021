from __future__ import annotations
from .car import Car
import copy
# DEBUG=True
DEBUG=False
class Street:

	def __init__(self, i1: int, i2: int, name: str, time: int ):
		super().__init__()
		self.name = name
		self.time = time
		self.i1 = i1
		self.i2 = i2
		self.delay = 0
		self.origin_cars = []
		self.car_to_add = []


	def __repr__(self):
		return "{} {} {} {}".format(self.i1, self.i2, self.name, self.time)

	def set_delay(self, delay: int):
		self.delay = delay

	def add_car_to_origin(self, car: Car):
		self.origin_cars.append((0, car))

	def reset_cars(self):
		self.cars = [*self.origin_cars]

	def next(self):
		# Add previous add cars
		self.cars += self.car_to_add
		self.car_to_add = []


		score = 0
		i_car = None
		for j in range(0, len(self.cars)):
			car = self.cars[j]
			if car[0] <= 0:
				i_car = j
				break

		if (i_car != None):
			car = (self.cars[i_car])[1]
			if car.road_map[-1] == self:
				self.print("\t\tCar has finished")
				score = 1
			else:
				# Add in next street
				index = car.road_map.index(self)
				next_street = car.road_map[index + 1]
				next_street.add_car_to_add(car)
				
				self.print("\t\tMove car from {} to {}".format(self.name, next_street.name))
				# Remove from here
				# print("Before {}".format(len(self.cars)))
				self.cars.pop(i_car)
				# print("After {}".format(len(self.cars)))

		self.cars = [(car[0] - 1, car[1]) for car in self.cars]
		return score
		
	# def add_car(self, car: Car):
	# 	self.cars.append((self.time, car))

	def add_car_to_add(self, car: Car):
		self.car_to_add.append((self.time, car))
		
	def __eq__(self, value):
		return value != None and self.name == value.name
	
	def print(self, message: str = ""):
		if DEBUG:
			print(message)
	# 	pass